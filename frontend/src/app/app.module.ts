import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import { TopBarComponent } from './shared/top-bar/top-bar.component';
import { BottomBarComponent } from './shared/bottom-bar/bottom-bar.component';

import { MainPageComponent } from './main-page/main-page.component';
import { AdminPageComponent } from './admin-page/admin-page.component';
import { OnlineGamesPageComponent } from './online-games-page/online-games-page.component';
import { LocalGamesPageComponent } from './local-games-page/local-games-page.component';
import { TalkToBackendComponent } from './talk-to-backend/talk-to-backend.component';
import { CardSearchComponent } from './admin-page/card-search/card-search.component';
import { CardComponent } from './shared/card/card.component';
import { ImportExportControlsComponent } from './admin-page/import-export-controls/import-export-controls.component';
import { EditCardComponent } from './admin-page/edit-card/edit-card.component';
import { CardResultComponent } from './admin-page/card-search/card-result/card-result.component';
import { CardListComponent } from './shared/card-list/card-list.component';
import { CardPileComponent } from './shared/card-pile/card-pile.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatButtonModule } from '@angular/material/button';
import { MatDividerModule } from '@angular/material/divider';
import { MatIconModule } from '@angular/material/icon';
import { MatInputModule } from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';
import { FormsModule } from '@angular/forms';
import { MatTableModule } from '@angular/material/table';
import { MatPaginatorModule } from '@angular/material/paginator';
import { MatSortModule } from '@angular/material/sort';

@NgModule({
  declarations: [
    AppComponent,
    TopBarComponent,
    BottomBarComponent,
    MainPageComponent,
    TalkToBackendComponent,
    AdminPageComponent,
    CardSearchComponent,
    CardComponent,
    ImportExportControlsComponent,
    EditCardComponent,
    CardResultComponent,
    CardListComponent,
    CardPileComponent,
  ],
  imports: [BrowserModule, AppRoutingModule, CommonModule, HttpClientModule, BrowserAnimationsModule, MatButtonModule, MatDividerModule, MatIconModule, FormsModule, MatFormFieldModule, MatInputModule, MatTableModule, MatPaginatorModule, MatSortModule],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
