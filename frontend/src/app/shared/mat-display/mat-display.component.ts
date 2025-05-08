import {
  Component,
  Input,
  OnChanges,
  OnInit,
  SimpleChanges,
} from '@angular/core';
import { Subscription } from 'rxjs';

import { Card, MatZone } from 'src/app/models/card';
import { CardAPIService } from 'src/app/services/card-api.service';
import { GameStateService } from 'src/app/services/game-state.service';
import { MatListenerService } from 'src/app/services/mat-listener.service';

@Component({
  selector: 'mat-display',
  templateUrl: './mat-display.component.html',
  styleUrls: ['./mat-display.component.scss'],
})
export class MatDisplayComponent implements OnInit, OnChanges {
  @Input() matId: string | null = null;
  /** This enables card edits, (re)pairing, and showing unpaired cards */
  @Input() admin: boolean = false;
  /** Optional name for the header. Uses matId if null. */
  @Input() playerName: string | null = null;

  public readonly placeholderImgSrc: string;

  public pairedCards: Card[] = [];
  public unpairedCards: Card[] = [];

  public get battlefieldCards(): Card[] {
    return this.pairedCards.filter((c) => c.zone === MatZone.BATTLEFIELD);
  }
  public get commandCards(): Card[] {
    return this.pairedCards.filter((c) => c.zone === MatZone.COMMAND);
  }
  public get exileCards(): Card[] {
    return this.pairedCards.filter((c) => c.zone === MatZone.EXILE);
  }
  public get graveyardCards(): Card[] {
    return this.pairedCards.filter((c) => c.zone === MatZone.GRAVEYARD);
  }
  public get libraryCards(): Card[] {
    return this.pairedCards.filter((c) => c.zone === MatZone.LIBRARY);
  }
  public get notPresentCards(): Card[] {
    return this.pairedCards.filter((c) => c.zone === MatZone.NOT_PRESENT);
  }

  private cardsSubscription: Subscription | null = null;

  constructor(
    private readonly cardAPIService: CardAPIService,
    private readonly matListener: MatListenerService
  ) {
    this.placeholderImgSrc = this.cardAPIService.getEmptyStackPlaceholderURL();
  }

  public ngOnInit(): void {
    this.resetCardsSubscription(this.matId);
  }

  public ngOnChanges(changes: SimpleChanges): void {
    if (changes['matId']) {
      this.resetCardsSubscription(changes['matId'].currentValue);
    }
  }

  private resetCardsSubscription(matId: string | null) {
    this.cardsSubscription?.unsubscribe();
    let cards$ = this.matListener.getCards$();
    if (matId) {
      cards$ = this.matListener.getCardsForMat$(matId);
    }

    this.cardsSubscription = cards$.subscribe((cardList) => {
      this.pairedCards = cardList.filter((c) => c.api_id !== null);
      this.unpairedCards = cardList.filter((c) => c.api_id === null);
    });
  }
}
