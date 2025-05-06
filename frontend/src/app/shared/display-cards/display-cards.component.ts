import { Component, Input } from '@angular/core';

import { Card } from 'src/app/models/card';
import { GameStateService } from 'src/app/services/game-state.service';

@Component({
  selector: 'display-cards',
  templateUrl: './display-cards.component.html',
  styleUrls: ['./display-cards.component.scss'],
})
export class DisplayCardsComponent {
  @Input() showUnpairedCards: boolean = false;
  @Input() allowEdit: boolean = false;

  public cards: Card[] = [];

  constructor(private readonly gameStateService: GameStateService) {
    //this.refreshCardList();
    GameStateService.cards.subscribe((cardList) => (this.cards = cardList));
  }

  public refreshCardList() {
    this.gameStateService
      .getAllCards()
      .subscribe((cardList) => (this.cards = cardList));
  }
}
