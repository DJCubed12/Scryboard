import { Injectable } from '@angular/core';
import { Observable, Subject } from 'rxjs';

import { io } from 'socket.io-client';
import { BACKEND_URL } from 'src/constants';
import { Card } from '../models/card';

@Injectable({
  providedIn: 'root',
})
export class MatListenerService {
  private readonly socket = io(BACKEND_URL);
  private readonly cards: Subject<Card[]> = new Subject<Card[]>();

  constructor() {
    this.socket.on('connect', () => {
      console.log('Connected to server!');
    });

    this.socket.on('message', (msg: string) => {
      console.log('Server msg: ', msg);
    });

    this.socket.on('cardUpdate', (cards: Card[]) => {
      console.log('Handling cardUpdate!: ', cards);
      //var cards = <Card[]>JSON.parse(data[0]);
      this.cards.next(cards);
    });

    this.socket.on('connect_error', (err) => {
      // the reason of the error, for example "xhr poll error"
      console.log(err.message);
    });
  }

  public getCards$(): Observable<Card[]> {
    return this.cards;
  }
}
