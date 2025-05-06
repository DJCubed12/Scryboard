import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

import { map, Observable, pipe, Subject } from 'rxjs';

import { Card, MatZone } from '../models/card';
import { BACKEND_URL } from 'src/constants';

import { io } from 'socket.io-client';
import { AppComponent } from '../app.component';
const socket = io(BACKEND_URL);

socket.on('connect', () => {
  console.log('Connected to server!');
});

socket.on('message', (msg: string) => {
  console.log("Server msg: ", msg);
});

socket.on('cardUpdate', (cards: Card[]) => {
  console.log("Handling cardUpdate!: ", cards);
  //var cards = <Card[]>JSON.parse(data[0]);
  //GameStateService.cards.next(cards);
});

socket.on("connect_error", (err) => {
  // the reason of the error, for example "xhr poll error"
  console.log(err.message);
});


@Injectable({
  providedIn: 'root',
})
export class GameStateService {
  constructor(private readonly http: HttpClient) {}

  static cards: Subject<Card[]> = new Subject<Card[]>();

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

  public setZone(
    rfid: string,
    zone: MatZone | null
  ): Observable<{ success: string }> {
    const body = { zone };
    return this.http.patch<{ success: string }>(
      BACKEND_URL + `card/${rfid}/zone`,
      body
    );
  }
}
