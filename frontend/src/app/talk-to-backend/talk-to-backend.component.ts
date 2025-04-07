import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';
import { BACKEND_URL } from 'src/constants';

@Component({
  selector: 'talk-to-backend',
  templateUrl: './talk-to-backend.component.html',
  styleUrls: ['./talk-to-backend.component.scss'],
})
export class TalkToBackendComponent {
  /** A variable that is pulled by the component.html file and displayed. */
  public backendMessage: string = 'Backend response will appear here...';

  constructor(private readonly http: HttpClient) {}

  /** Called from within the component.html file */
  public talkToBackend() {
    // Sends a GET request at the specified URL (http://localhost:5000/data), and expects a response that has a string 'msg'.
    this.http.get<{ msg: string }>(BACKEND_URL + 'data').subscribe(
      // This code is run when we get the response
      (response) => (this.backendMessage = response['msg']),
      // This code is run when an error occurs (like a timeout for example)
      (error) => {
        // You can see console.log and console.error messages in the Browser console. Do ctrl+shft+i and click on the "Console" tab
        console.error(`Oh no! There was an error! ${error}`);
        this.backendMessage =
          'Uh oh. Something went wrong. Are you sure the backend is running?';
      }
    );
  }
}
