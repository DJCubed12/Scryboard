import {
  Component,
  Input,
  OnChanges,
  OnInit,
  SimpleChanges,
} from '@angular/core';
import { Subscription } from 'rxjs';

import { Card, MatZone } from 'src/app/models/card';
import { GameStateService } from 'src/app/services/game-state.service';
import { MatListenerService } from 'src/app/services/mat-listener.service';

@Component({
  selector: 'mat-display',
  templateUrl: './mat-display.component.html',
  styleUrls: ['./mat-display.component.scss'],
})
export class MatDisplayComponent implements OnInit, OnChanges {
  @Input() matId: string | null = null;
  @Input() showUnpairedCards: boolean = false;
  @Input() allowEdit: boolean = false;

  public cards: Card[] = [];

  public get battlefieldCards(): Card[] {
    return this.cards.filter((c) => c.zone === MatZone.BATTLEFIELD);
  }
  public get commandCards(): Card[] {
    return this.cards.filter((c) => c.zone === MatZone.COMMAND);
  }
  public get exileCards(): Card[] {
    return this.cards.filter((c) => c.zone === MatZone.EXILE);
  }
  public get graveyardCards(): Card[] {
    return this.cards.filter((c) => c.zone === MatZone.GRAVEYARD);
  }
  public get libraryCards(): Card[] {
    return this.cards.filter((c) => c.zone === MatZone.LIBRARY);
  }
  public get notPresentCards(): Card[] {
    return this.cards.filter((c) => c.zone === MatZone.NOT_PRESENT);
  }

  private cardsSubscription: Subscription | null = null;

  constructor(
    private readonly gameStateService: GameStateService,
    private readonly matListener: MatListenerService
  ) {}

  public ngOnInit(): void {
    this.resetCardsSubscription(this.matId);
  }

  public ngOnChanges(changes: SimpleChanges): void {
    if (changes['matId']) {
      this.resetCardsSubscription(changes['matId'].currentValue);
    }
  }

  public refreshCardList() {
    this.gameStateService
      .getAllCards()
      .subscribe((cardList) => (this.cards = cardList));
  }

  private resetCardsSubscription(matId: string | null) {
    this.cardsSubscription?.unsubscribe();
    if (matId) {
      this.cardsSubscription = this.matListener
        .getCardsForMat$(matId)
        .subscribe((cardList) => (this.cards = cardList));
    } else {
      this.cardsSubscription = this.matListener
        .getCards$()
        .subscribe((cardList) => (this.cards = cardList));
    }
  }
}
