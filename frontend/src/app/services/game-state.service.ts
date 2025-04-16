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

  public pairAPIId(
    rfid: string,
    api_id: string
  ): Observable<{ success: string }> {
    const body = { api_id };
    return this.http.patch<{ success: string }>(
      BACKEND_URL + `/card/${rfid}`,
      body
    );
  }
}
