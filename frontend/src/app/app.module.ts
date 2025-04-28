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
import { DisplayCardsComponent } from './shared/display-cards/display-cards.component';
import { CardComponent } from './shared/display-cards/card/card.component';
import { ImportExportControlsComponent } from './admin-page/import-export-controls/import-export-controls.component';

@NgModule({
  declarations: [
    AppComponent,
    TopBarComponent,
    BottomBarComponent,
    MainPageComponent,
    TalkToBackendComponent,
    AdminPageComponent,
    CardSearchComponent,
    DisplayCardsComponent,
    CardComponent,
    ImportExportControlsComponent,
  ],
  imports: [BrowserModule, AppRoutingModule, CommonModule, HttpClientModule],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
