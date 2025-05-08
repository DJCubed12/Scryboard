import { Component, Input } from '@angular/core';
import { Card } from 'src/app/models/card';
import { CardAPIService } from 'src/app/services/card-api.service';

@Component({
  selector: 'card-pile',
  templateUrl: './card-pile.component.html',
  styleUrls: ['./card-pile.component.scss'],
})
export class CardPileComponent {
  @Input() cards: Card[] = [];

  public readonly placeholderImgSrc;

  constructor(private readonly cardAPIService: CardAPIService) {
    this.placeholderImgSrc = this.cardAPIService.getEmptyStackPlaceholderURL();
  }

  public debugPrint() {
    console.log('Cards in pile are:', this.cards);
  }
}
