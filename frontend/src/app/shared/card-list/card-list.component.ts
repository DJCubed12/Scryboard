import { Component, Input } from '@angular/core';

import { Card } from 'src/app/models/card';

@Component({
  selector: 'card-list',
  templateUrl: './card-list.component.html',
  styleUrls: ['./card-list.component.scss'],
})
export class CardListComponent {
  @Input() cards: Card[] = [];
  @Input() allowEdit: boolean = false;
  @Input() debug: boolean = false;
}
