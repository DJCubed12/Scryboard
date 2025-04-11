import { Component } from '@angular/core';

import { CardAPIService } from 'src/app/services/external-api.service';

@Component({
  selector: 'card-search',
  templateUrl: './card-search.component.html',
  styleUrls: ['./card-search.component.scss'],
})
export class CardSearchComponent {
  public results: any = undefined;

  constructor(private readonly cardAPI: CardAPIService) {}

  public searchByTitle(cardTitle: string) {
    this.cardAPI.searchByTitle('profane').subscribe(
      (response) => (this.results = response),
      (error) => {
        console.error(error);
        this.results = error;
      }
    );
  }
}
