import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';
import { BACKEND_URL } from 'src/constants';

@Component({
  selector: 'talk-to-backend',
  templateUrl: './talk-to-backend.component.html',
  styleUrls: ['./talk-to-backend.component.scss'],
})
export class TalkToBackendComponent {
  public backendMessage: string = '';

  constructor(private readonly http: HttpClient) {}

  public talkToBackend() {
    this.http.get<{ msg: string }>(BACKEND_URL + 'data').subscribe(
      (message) => (this.backendMessage = message['msg']),
      (error) => {
        console.error(`Oh no! There was an error! ${error}`);
        this.backendMessage =
          'Uh oh. Something went wrong. Are you sure the backend is running?';
      }
    );
  }
}
