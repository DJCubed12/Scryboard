import {
  Component,
  Input,
  OnChanges,
  OnInit,
  SimpleChanges,
} from '@angular/core';
import { Subscription } from 'rxjs';

import { Card } from 'src/app/models/card';
import { GameStateService } from 'src/app/services/game-state.service';
import { MatListenerService } from 'src/app/services/mat-listener.service';

@Component({
  selector: 'card-list',
  templateUrl: './card-list.component.html',
  styleUrls: ['./card-list.component.scss'],
})
export class CardListComponent implements OnInit, OnChanges {
  @Input() matId: string | null = null;
  @Input() showUnpairedCards: boolean = false;
  @Input() allowEdit: boolean = false;
  @Input() debug: boolean = false;

  public cards: Card[] = [];

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
