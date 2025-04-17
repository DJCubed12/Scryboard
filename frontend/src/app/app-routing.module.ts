import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { MainPageComponent } from './main-page/main-page.component';
import { AdminPageComponent } from './admin-page/admin-page.component';
import { CardSearchComponent } from './admin-page/card-search/card-search.component';

const routes: Routes = [
  {
    path: 'admin',
    children: [
      {
        path: '',
        component: AdminPageComponent,
      },
      {
        path: 'pair/:rfid',
        component: CardSearchComponent,
      },
    ],
  },
  {
    // The default route
    path: '**',
    component: MainPageComponent,
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
