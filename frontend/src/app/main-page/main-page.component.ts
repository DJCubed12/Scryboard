import { Component } from '@angular/core';
import { GameStateService } from '../services/game-state.service';

@Component({
  selector: 'main-page',
  templateUrl: './main-page.component.html',
  styleUrls: ['./main-page.component.scss'],
})
export class MainPageComponent {
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
