import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

import { map, Observable } from 'rxjs';

import { Card } from '../models/card';
import { BACKEND_URL } from 'src/constants';

@Injectable({
  providedIn: 'root',
})
export class GameStateService {
  constructor(private readonly http: HttpClient) {}

  public getAllCards(): Observable<Card[]> {
    return this.http
      .get<{ cards: Card[] }>(BACKEND_URL + '/cards')
      .pipe(map((msg: { cards: Card[] }) => msg.cards));
  }
}
