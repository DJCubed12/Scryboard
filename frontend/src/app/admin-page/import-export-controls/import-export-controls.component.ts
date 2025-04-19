import { Component } from '@angular/core';

import { ImportExportService } from 'src/app/services/import-export.service';

@Component({
  selector: 'import-export-controls',
  templateUrl: './import-export-controls.component.html',
  styleUrls: ['./import-export-controls.component.scss'],
})
export class ImportExportControlsComponent {
  constructor(private readonly importExportService: ImportExportService) {}

  public export(
    matId: string | null = null,
    filename: string = 'scryboard-export.json'
  ) {
    this.importExportService
      .getExportFileDownloadLink$(matId)
      .subscribe((fileURL: string) => {
        const downloadLink = document.createElement('a');
        downloadLink.href = fileURL;
        downloadLink.setAttribute('download', filename);
        downloadLink.setAttribute('target', '_blank');
        document.body.appendChild(downloadLink);
        downloadLink.click();
        downloadLink.remove();
      });
  }
}
