import { Component, Input } from '@angular/core';

import { Card } from 'src/app/models/card';
import { CardAPIService } from 'src/app/services/card-api.service';

@Component({
  selector: 'card',
  templateUrl: './card.component.html',
  styleUrls: ['./card.component.scss'],
})
export class CardComponent {
  @Input() card!: Card;
  @Input() debug: boolean = false;

  constructor(private readonly cardAPIService: CardAPIService) {}

  public getCardImage(): string {
    if (this.card.is_face_up && this.card.front_image) {
      return this.card.front_image;
    } else if (!this.card.is_face_up && this.card.back_image) {
      return this.card.back_image;
    } else {
      // Fallback to just default card back image
      return this.cardAPIService.getDefaultCardBackURL();
    }
  }
}
