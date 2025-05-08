import { Component, Input } from '@angular/core';

import { Card } from 'src/app/models/card';
import { GameStateService } from 'src/app/services/game-state.service';

@Component({
  selector: 'card-list',
  templateUrl: './card-list.component.html',
  styleUrls: ['./card-list.component.scss'],
})
export class CardListComponent {
  @Input() cards: Card[] = [];
  @Input() allowEdit: boolean = false;
  @Input() debug: boolean = false;

  constructor(private readonly gameStateService: GameStateService) {}

  public flip(card: Card) {
    if (this.allowEdit) {
      this.gameStateService.flipCard(card.rfid, !card.is_face_up).subscribe();
    }
  }
}
