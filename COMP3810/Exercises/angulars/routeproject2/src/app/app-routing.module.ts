import { NgModule } from '@angular/core';
import { RouterModule, Routes} from '@angular/router';
import { AboutComponent } from './about/about.component';
import { HomeComponent } from './home/home.component';
import { AdminComponent } from './admin/admin.component';
import { RouteErrorComponent } from './error/route.error.component';

const appRoutes: Routes = [
    {path: 'home', component: HomeComponent}
    ,{path: 'about', component: AboutComponent }
    ,{path: 'admin', component: AdminComponent }
    ,{path: 'error', component: RouteErrorComponent }
    ,{path: '**', redirectTo: '/error'}
];

@NgModule({
    imports: [ RouterModule.forRoot(appRoutes) ],
    exports: [ RouterModule],
    providers: [ ]
})

export class AppRoutingModule {}

