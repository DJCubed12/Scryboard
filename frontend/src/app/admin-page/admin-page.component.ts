import { Component } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';

import { CardAPIService } from 'src/app/services/card-api.service';
import { GameStateService } from 'src/app/services/game-state.service';

@Component({
  selector: 'admin-page',
  templateUrl: './admin-page.component.html',
  styleUrls: ['./admin-page.component.scss'],
})
export class AdminPageComponent {
  public mats: string[] = [];

  constructor(private readonly gameStateService: GameStateService) {
    this.refreshMatList();
  }

  public refreshMatList() {
    this.gameStateService
      .getMats()
      .subscribe((matList) => (this.mats = matList));
  }
}
