import { Component } from '@angular/core';

import { MatListenerService } from '../services/mat-listener.service';

@Component({
  selector: 'admin-page',
  templateUrl: './admin-page.component.html',
  styleUrls: ['./admin-page.component.scss'],
})
export class AdminPageComponent {
  public mats: string[] = [];

  constructor(private readonly matListener: MatListenerService) {
    this.matListener.getMats$().subscribe((matList) => (this.mats = matList));
  }
}
