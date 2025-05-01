import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { PairData } from 'src/app/models/card';

import { CardAPIService } from 'src/app/services/card-api.service';
import { GameStateService } from 'src/app/services/game-state.service';

@Component({
  selector: 'card-search',
  templateUrl: './card-search.component.html',
  styleUrls: ['./card-search.component.scss'],
})
export class CardSearchComponent implements OnInit {
  public results: any = undefined;
  public cards: any = [];
  /** The RFID that the chosen card will be associated with. */
  public rfid: string | null = null;

  constructor(
    private readonly cardAPI: CardAPIService,
    private readonly gameStateService: GameStateService,
    private readonly route: ActivatedRoute,
    private readonly router: Router
  ) {}

  public ngOnInit(): void {
    this.rfid = this.route.snapshot.paramMap.get('rfid');
  }

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

  public pairAPIId(pairData: PairData) {
    if (this.rfid === null) {
      console.error('Error: Can not pair without an RFID (rfid is null)');
      return;
    } else if (pairData.api_id === undefined) {
      console.error("Error: Can't find card's ID.");
    }

    this.gameStateService
      .pairAPIId(
        this.rfid,
        pairData.api_id,
        pairData.front_image,
        pairData.back_image
      )
      .subscribe(
        (resp) => {
          console.log('Successfully updated API ID!');
          this.router.navigate(['/admin']);
        },
        (err) =>
          console.error(`Error updating API ID for card RFID=${this.rfid}`, err)
      );
  }
}
