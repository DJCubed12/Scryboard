import { Component, Input } from '@angular/core';

import { Card } from 'src/app/models/card';

@Component({
  selector: 'card',
  templateUrl: './card.component.html',
  styleUrls: ['./card.component.scss'],
})
export class CardComponent {
  @Input() card!: Card;

  constructor() {}
}
