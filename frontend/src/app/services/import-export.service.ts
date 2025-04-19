import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { map, Observable } from 'rxjs';

import { BACKEND_URL } from 'src/constants';

@Injectable({
  providedIn: 'root',
})
export class ImportExportService {
  constructor(private readonly http: HttpClient) {}

  public getExportFileDownloadLink$(
    matId: string | null = null
  ): Observable<string> {
    let exportURL = BACKEND_URL + 'cards/';
    if (matId) {
      exportURL += matId + '/';
    }
    exportURL += 'export';

    return this.http
      .get<Blob>(exportURL, { responseType: 'blob' as 'json' })
      .pipe(
        map((response: Blob) => {
          const dataType = response.type;
          if (dataType !== 'application/json') {
            throw new TypeError(
              `Received '${dataType}' response when expecting 'application/json'.`
            );
          }

          let binaryData = [];
          binaryData.push(response);
          return window.URL.createObjectURL(
            new Blob(binaryData, { type: dataType })
          );
        })
      );
  }

  public sendImportFile$(file: File) {
    const formData: FormData = new FormData();
    formData.append('importFile', file, file.name);

    return this.http.post(BACKEND_URL + '/cards', formData);
  }
}
