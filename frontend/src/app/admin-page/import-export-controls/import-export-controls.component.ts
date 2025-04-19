import { Component } from '@angular/core';

import { ImportExportService } from 'src/app/services/import-export.service';

@Component({
  selector: 'import-export-controls',
  templateUrl: './import-export-controls.component.html',
  styleUrls: ['./import-export-controls.component.scss'],
})
export class ImportExportControlsComponent {
  private importFile: File | null = null;

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

  public changeImportFile(e: Event) {
    let fileList: FileList | null = (e.target as any).files;
    if (fileList && fileList.length >= 1) {
      this.importFile = fileList[0];
    }
  }

  public import() {
    if (this.importFile) {
      this.importExportService.sendImportFile$(this.importFile).subscribe(
        // TODO: Resp will contain the updated card list; this could be used to immediately update the frontend's list, instead of waiting for the user to click refresh
        (resp) => console.log(resp),
        (err) => console.error('Error while importing from file', err)
      );
    }
  }
}
