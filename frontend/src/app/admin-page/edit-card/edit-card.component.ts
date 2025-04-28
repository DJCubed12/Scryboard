import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Card } from 'src/app/models/card';
import { GameStateService } from 'src/app/services/game-state.service';

@Component({
  selector: 'edit-card',
  templateUrl: './edit-card.component.html',
  styleUrls: ['./edit-card.component.scss'],
})
export class EditCardComponent {
  public rfid: string | null = null;
  public card: Card | null = null;

  constructor(
    private readonly gameStateService: GameStateService,
    private readonly route: ActivatedRoute
  ) {}

  public ngOnInit(): void {
    this.rfid = this.route.snapshot.paramMap.get('rfid');
  }
}
