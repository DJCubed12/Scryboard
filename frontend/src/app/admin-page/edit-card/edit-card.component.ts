import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Card, MatZone } from 'src/app/models/card';
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
    this.reloadCard();
  }

  public reloadCard() {
    this.gameStateService.getCard(this.rfid!).subscribe(
      (card) => (this.card = card),
      (err) => console.error(err)
    );
  }

  public setZone(zone: string) {
    let matZone: MatZone | null = null;
    if (zone) {
      matZone = zone as MatZone;
    }

    this.gameStateService
      .setZone(this.rfid!, matZone)
      .subscribe((msg) => this.reloadCard());
  }

  public flip() {
    this.gameStateService
      .flipCard(this.rfid!, !this.card?.is_face_up)
      .subscribe((msg) => this.reloadCard());
  }
}
