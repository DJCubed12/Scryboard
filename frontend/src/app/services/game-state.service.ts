import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

import { map, Observable } from 'rxjs';

import { Card, MatZone } from '../models/card';
import { BACKEND_URL } from 'src/constants';

@Injectable({
  providedIn: 'root',
})
export class GameStateService {
  constructor(private readonly http: HttpClient) {}

  public getAllCards(): Observable<Card[]> {
    return this.http
      .get<{ cards: Card[] }>(BACKEND_URL + 'cards')
      .pipe(map((msg: { cards: Card[] }) => msg.cards));
  }

  public getCard(rfid: string): Observable<Card> {
    return this.http
      .get<{ card: Card }>(BACKEND_URL + 'card/' + rfid)
      .pipe(map((msg: { card: Card }) => msg.card));
  }

  public pairAPIId(
    rfid: string,
    api_id: string,
    front_image: string | null = null,
    back_image: string | null = null
  ): Observable<{ success: string }> {
    const body = { api_id, front_image, back_image };
    return this.http.patch<{ success: string }>(
      BACKEND_URL + `card/${rfid}/pair`,
      body
    );
  }

  public flipCard(
    rfid: string,
    to_face_up: boolean
  ): Observable<{ success: string }> {
    const body = { to_face_up };
    return this.http.patch<{ success: string }>(
      BACKEND_URL + `card/${rfid}/flip`,
      body
    );
  }

  public setZone(rfid: string, zone: MatZone): Observable<{ success: string }> {
    const body = { zone };
    return this.http.patch<{ success: string }>(
      BACKEND_URL + `card/${rfid}/zone`,
      body
    );
  }
}
