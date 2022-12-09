import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable, ErrorHandler } from '@angular/core';
import { Observable, interval, throwError } from 'rxjs';
import { retry, catchError } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})

export class QuestionService {
    // Define API
    apiURL = 'http://localhost:3000';
    constructor(private http: HttpClient) {}
    httpOptions = {
        headers: new HttpHeaders({
        'Content-Type': 'application/json',
        }),
    };

    getQuestionJson(): Observable<string[]>{
       return this.http.get<string[]>(this.apiURL + '/questions')
      .pipe(retry(1), catchError(this.handleError));
    }
    handleError(error: any) {
        let errorMessage = '';
        if (error.error instanceof ErrorEvent) {
            // Get client-side error
            errorMessage = error.error.message;
        } else {
            // Get server-side error
            errorMessage = `Error Code: ${error.status}\nMessage: ${error.message}`;
        }
        window.alert(errorMessage);
        return throwError(() => {
            return errorMessage;
        });
    }
}
