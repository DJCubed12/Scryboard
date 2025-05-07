import { Component, Input } from '@angular/core';

import { Card } from 'src/app/models/card';
import { CardAPIService } from 'src/app/services/card-api.service';
import { GameStateService } from 'src/app/services/game-state.service';
import { MatListenerService } from 'src/app/services/mat-listener.service';

@Component({
  selector: 'card-list',
  templateUrl: './card-list.component.html',
  styleUrls: ['./card-list.component.scss'],
})
export class CardListComponent {
  @Input() showUnpairedCards: boolean = false;
  @Input() allowEdit: boolean = false;

  public cards: Card[] = [];

  constructor(
    private readonly gameStateService: GameStateService,
    private readonly matListener: MatListenerService
  ) {
    //this.refreshCardList();
    this.matListener.getCards$().subscribe((cardList) => {
      this.cards = [];
      this.cards = cardList;
    });
  }

  public refreshCardList() {
    this.gameStateService
      .getAllCards()
      .subscribe((cardList) => (this.cards = cardList));
  }
}
