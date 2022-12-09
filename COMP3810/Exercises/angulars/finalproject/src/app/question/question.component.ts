import { Component, OnInit } from '@angular/core';
import { QuestionService } from '../../../server/question.service';
import { Observable, interval, throwError } from 'rxjs';

@Component({
  selector: 'app-question',
  templateUrl: './question.component.html',
  styleUrls: ['./question.component.scss']
})
export class QuestionComponent {
    //variables
    name: string;
    questionList: any[];
    currentQuestion: number;
    points: number;
    counter: number;
    correctAnswer: number;
    inCorrectAnswer:number;
    interval$: any;
    progress: string;
    isQuizCompleted: boolean;

    //ctor
    constructor(public questionService: QuestionService) { 
        this.name = '';
        this.questionList = [];
        this.currentQuestion = 0;
        this.points = 0;
        this.counter = 30;
        this.correctAnswer = 0;
        this.inCorrectAnswer = 0;
        this.interval$ = '';
        this.progress = '0';
        this.isQuizCompleted = false;
    }
    
    ngOnInit(name: string){
        this.name = name;
        this.getAllQuestions();
        this.startCounter();
    }    
    
    getAllQuestions(){
        return this.questionService.getQuestionJson().subscribe((res) => {
           this.questionList = res; 
        });
    }
    nextQuestion(){
        this.currentQuestion += 1;
    }
    previousQuestion(){
        this.currentQuestion -= 1;
    }
    answer(quesNum: number, option: any){
        if (quesNum > this.questionList.length){
            this.isQuizCompleted = true;
            this.stopCounter();
        } else {
            if (option.correct) {
                this.points += 5;
                this.correctAnswer++;
                setTimeout(() => {
                    this.currentQuestion++;
                    this.resetCounter();
                    this.getProgressPercent();
                }, 1000);
            } else {
                setTimeout(() => {
                    this.currentQuestion++;
                    this.inCorrectAnswer++;
                    this.resetCounter();
                    this.getProgressPercent();
                }, 1000);
                this.points -=0;
            }   
        }
    }
    startCounter() {
        this.interval$ = interval(1000).subscribe(val => {
            this.counter--;
            if (this.counter === 0) {
                this.currentQuestion++;
                this.counter = 30;
                this.points -= 0;
            }
        });
        setTimeout(() => {
            this.interval$.unsubscribe();
        }, 600000);
    }
    stopCounter() {
        this.interval$.unsubscribe();
        this.counter = 0;
    }    
    resetCounter(){
        this.stopCounter();
        this.counter = 30;
        this.startCounter();
    }
    resetQuiz(){
        this.resetCounter();
        this.getAllQuestions();
        this.points = 0;
        this.currentQuestion = 0;
        this.progress = '0';
    }
    getProgressPercent(){
        this.progress = ((this.currentQuestion / this.questionList.length) * 100) + ""; 
        return this.progress
    }
}
