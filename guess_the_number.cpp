#include<iostream>
#include<ctime>
int main(){
    srand(time(0));
    int range_min , range_max,choice;
    while(true){
        std::cout<<"1)you guess\n2)computer guess\n3)end\n";
        std::cout<<"enter your choice : ";
        std::cin>>choice;
        if(choice==1){
            int guess,no_guess=0;
            std::cout<<"enter minimum and maximum range : ";
            std::cin>>range_min>>range_max;
            int ran_num=rand()%(range_max-(range_min-1))+(range_min-1)+1;
            
            do{
                std::cout<<"guess the number ";
                std::cin>>guess;
                no_guess++;
                if(guess>ran_num){std::cout<<"try less !\n";}
                else if(guess<ran_num){std::cout<<"try higher !\n";}
            }while(guess!=ran_num);
            std::cout<<"you found in "<<no_guess<<"th chance"<<'\n';
        }
        else if(choice==2){
            int num,no_cpu=0;
            std::cout<<"enter minimum and maximum range : ";
            std::cin>>range_min>>range_max;
            int ran_num;
            std::cout<<"enter a number for computer to guess : ";
            std::cin>>num;
            do{
                ran_num=rand()%(range_max-(range_min-1))+(range_min-1)+1;
                no_cpu++;
                std::cout<<"is it "<<ran_num<<'\n';
                if(num>ran_num){
                    range_min=ran_num+1;
                    std::cout<<"try higher !\n";
                }
                else if(num<ran_num){
                    range_max=ran_num-1;
                    std::cout<<"try lesser !\n";
                }
                std::cout<<"min : "<<range_min<<" max : "<<range_max<<'\n';
            }while(num!=ran_num);
            std::cout<<"cpu found in "<<no_cpu<<"th chance"<<'\n';
        }
        else if(choice==3){break;}
        else{std::cout<<"enter the choice correctly!!!\n";}
    }
    return 0;
}