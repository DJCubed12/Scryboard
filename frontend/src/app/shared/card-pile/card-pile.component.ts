import { Component, Input } from '@angular/core';
import { Card } from 'src/app/models/card';

@Component({
  selector: 'card-pile',
  templateUrl: './card-pile.component.html',
  styleUrls: ['./card-pile.component.scss'],
})
export class CardPileComponent {
  @Input() cards: Card[] = [];

  public debugPrint() {
    console.log('Cards in pile are:', this.cards);
  }
}
