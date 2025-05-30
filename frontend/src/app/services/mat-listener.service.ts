import { Injectable } from '@angular/core';
import { BehaviorSubject, map, Observable } from 'rxjs';

import { io } from 'socket.io-client';
import { BACKEND_URL } from 'src/constants';
import { Card } from '../models/card';
import { GameStateService } from './game-state.service';

@Injectable({
  providedIn: 'root',
})
export class MatListenerService {
  private readonly socket = io(BACKEND_URL);
  private readonly mats: BehaviorSubject<string[]> = new BehaviorSubject<
    string[]
  >([]);
  private readonly cards: BehaviorSubject<Card[]> = new BehaviorSubject<Card[]>(
    []
  );

  constructor(private readonly gameStateService: GameStateService) {
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

    this.socket.on('matListUpdate', (matList: string[]) => {
      this.mats.next(matList.sort());
    });

    // Do normal HTTP requests to get initial values
    this.gameStateService
      .getMats()
      .subscribe((matList) => this.mats.next(matList.sort()));
    this.gameStateService
      .getAllCards()
      .subscribe((cards) => this.cards.next(cards));
  }

  public getMats$(): Observable<string[]> {
    return this.mats;
  }

  public getCards$(): Observable<Card[]> {
    return this.cards;
  }

  public getCardsForMat$(matId: string): Observable<Card[]> {
    return this.cards.pipe(
      map((cardList: Card[]) =>
        cardList.filter((card: Card) => card.mat_id === matId)
      )
    );
  }
}
