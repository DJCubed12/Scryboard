import { Component } from '@angular/core';

import { CardAPIService } from 'src/app/services/external-api.service';

@Component({
  selector: 'card-search',
  templateUrl: './card-search.component.html',
  styleUrls: ['./card-search.component.scss'],
})
export class CardSearchComponent {
  public results: any = undefined;
  public cards: any = [];

  constructor(private readonly cardAPI: CardAPIService) {}

  public searchByTitle(cardTitle: string) {
    this.cardAPI.searchByTitle(cardTitle).subscribe(
      (response) => {
        this.results = response;
        this.cards = response['data'];
      },
      (error) => {
        console.error(error);
        this.results = error;
      }
    );
  }

  public getCardImage(card: any): string | null {
    try {
      const image_url = card?.image_uris?.small;
      if (image_url) {
        return image_url;
      }
    } catch (TypeError) {
      // Card response doesn't follow normal format
    }
    return null;
  }
}
