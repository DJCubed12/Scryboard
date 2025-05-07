import { Component } from '@angular/core';
import { MatListenerService } from '../services/mat-listener.service';

@Component({
  selector: 'main-page',
  templateUrl: './main-page.component.html',
  styleUrls: ['./main-page.component.scss'],
})
export class MainPageComponent {
  public mats: string[] = [];

  constructor(private readonly matListener: MatListenerService) {
    this.matListener.getMats$().subscribe((matList) => (this.mats = matList));
  }
}
