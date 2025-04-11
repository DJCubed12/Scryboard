import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { EXTERNAL_API_URL } from 'src/constants';

@Injectable({
  providedIn: 'root',
})
export class CardAPIService {
  constructor(private readonly http: HttpClient) {}

  public searchByTitle(cardTitle: string): Observable<any> {
    return this.http.get(EXTERNAL_API_URL + 'cards/search', {
      params: {
        // Add URL Parameters here (everything after the ? in the URL)
        q: cardTitle,
      },
    });
  }
}
