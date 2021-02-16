#include<stdio.h>
#include<conio.h>
#include<string.h>
#include<math.h>
#include<ctype.h>
#include<windows.h>
#define GST_RATE 0.18

//To change the cursor to a Particular (x,y) coordinate
void gotoxy(int x, int y)
{
    COORD coord;
    coord.X = x;
    coord.Y = y;
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), coord);
}

//-------------GLOBAL VARIABLES-------------
int i, num_Dist=0, num_Med=10, num_Bill=0;

//---------------------FUNCTIONS---------------------
void main_menu();

//Layout of the screen
void box();
void box2();

void distributor();
void dist_list();
void dist_add();

void medicine();
void med_list();
void med_pur();
void med_sale();
void med_stock();

void bill();

void stock_alert();

void about();

//---------------------STRUCTURES---------------------
struct medicine
{
    int med_id;
    char medi_name[20];
    int quantity;
    float cost;
    float total;
}; //Defining a list of In-Built Medicines
struct medicine a[20] =
{
    {1,"Crocin", 100, 70},
    {2,"Paracetamol", 100, 62},
    {3,"Oxytocin", 100, 43},
    {4,"Advil", 100, 32},
    {5,"Abilify", 100, 93},
    {6,"Aspirin", 100, 67},
    {7,"Decadron", 100, 70},
    {8,"Dulera", 100, 23},
    {9,"Methotrexate", 100, 87},
    {10,"ursodiol", 100, 45}
};

struct distributor
{
    char dist_id[5];
    char dist_name[25];
    char city[20];
    char mob_no[11];
    char email[30];
};
struct distributor b[10];

struct bill
{
    char bill_id[3];
    char med_name[20];
    int quantity;
    float cost;
    float total;
};
struct bill bil[50];

//---------------LAYOUT OF THE MEDICAL STORE SITE---------------
void box()
{
    for(i=3 ; i<=90 ; i++)
    {
        gotoxy(i,7);
        printf("%c",205);
    }
    for(i=3; i<=90; i++)
    {
        gotoxy(i,3);
        printf("%c",220);
        gotoxy(89,45);
        printf("%c",220);
        gotoxy(i,45);
        printf("%c",220);
    }
    for(i=4; i<=45; i++)
    {
        gotoxy(3,i);
        printf("%c",219);
        gotoxy(90,i);
        printf("%c",219);
    }
}

void box2()
{
    gotoxy(36,5);
    printf("KJSCE MEDICAL STORE");
    gotoxy(7,9);
    printf("K. J. Somaiya College of Engineering");
    gotoxy(7,10);
    printf("Vidyanagar, Vidyavihar(E), Mumbai - 400 077, Maharashtra.");
    gotoxy(7,12);
    printf("Website : www.somaiya.edu/vidyavihar/kjsce/");
    gotoxy(7,13);
    printf("Email : enquiry@engg.somaiya.edu");

    for(i=3 ; i<=90 ; i++)
    {
        gotoxy(i,15);
        printf("%c",205);
    }
    for(i=3; i<=90; i++)
    {
        gotoxy(i,3);
        printf("%c",220);
        gotoxy(89,45);
        printf("%c",220);
        gotoxy(i,45);
        printf("%c",220);
    }
    for(i=4; i<=45; i++)
    {
        gotoxy(3,i);
        printf("%c",219);
        gotoxy(90,i);
        printf("%c",219);
    }
}
//--------------Main--------------
int main()
{
    main_menu();
}

//---------------DISPLAY THE HOMEPAGE OF THE SITE---------------
void main_menu()
{
    char ch;
    do
    {
        system("cls");
        gotoxy(5,5);
        printf("Distributor Info(D)");
        gotoxy(28,5);
        printf("Medicine(M)");
        gotoxy(42,5);
        printf("Bill(B)");
        gotoxy(52,5);
        printf("Stock Alert(S)");
        gotoxy(70,5);
        printf("About(A)");
        gotoxy(81,5);
        printf("Exit(E)");
        gotoxy(33,17);
        printf("WELCOME TO KJSCE MEDICAL STORE");
        box();
        gotoxy(25,25);
        printf("Press the first character for further Menu : ");
        ch=toupper(getche());
        switch(ch)
        {
        case 'D':
            distributor();
            break;
        case 'M':
            medicine();
            break;
        case 'B':
            bill();
            break;
        case 'S':
            stock_alert();
            break;
        case 'A':
            about();
            break;
        case 'E':
            exit(0);
        default:
            gotoxy(25,28);
            printf("Please enter character from (D,M,B,S,A,E).");
        }
    }
    while(ch !='E');
}

//--------------FOR DISTRIBUTOR--------------
void distributor()
{
    char ch;
    do
    {
        system("cls");
        gotoxy(40,5);
        printf("DISTRIBUTOR MENU");
        gotoxy(7,10);
        printf("Distributor List(L)");
        gotoxy(7,13);
        printf("Add New Distributor(A)");
        gotoxy(7,16);
        printf("Main Menu(M)");
        box();
        gotoxy(19,25);
        printf("Press the character in brackets for further operation : ");
        ch=toupper(getche());
        switch(ch)
        {
        case 'L':
            dist_list();
            break;
        case 'A':
            dist_add();
            break;
        case 'M':
            main_menu();
            break;
        default:
            gotoxy(19,29);
            printf("Please enter character from (L,A,M).");
        }
    }
    while(ch!='M');
}

//--------------FOR MEDICINE--------------
void medicine()
{
    char ch;
    do
    {
        system("cls");
        gotoxy(39,5);
        printf("MEDICINE");
        gotoxy(7,10);
        printf("Medicine List(L)");
        gotoxy(7,13);
        printf("Purchase New Medicine(P)");
        gotoxy(7,16);
        printf("Stock of Medicine(S)");
        gotoxy(7,19);
        printf("Sale of Medicine(C)");
        gotoxy(7,22);
        printf("Main Menu(M)");
        box();
        gotoxy(19,25);
        printf("Press the character in brackets for further operation : ");
        ch=toupper(getche());
        switch(ch)
        {
        case 'L':
            med_list();
            break;
        case 'P':
            med_pur();
            break;
        case 'S':
            med_stock();
            break;
        case 'C':
            med_sale();
        case 'M':
            main_menu();
            break;
        default:
            gotoxy(19,29);
            printf("Please enter character from(L,P,S,C,M).");
        }
    }
    while(ch!='M');
}

//--------------FOR BILL--------------
void bill()
{
    int j, n;
    float sum=0;
    system("cls");
    gotoxy(46,17);
    printf("BILL");
    box2();
    gotoxy(15,19);
    printf("SrNo.       MEDICINE NAME.      RATE.      QUANTITY       TOTAL");
    i=21;
    for(j=0 ; j<num_Bill ; j++)
    {
        gotoxy(15,i);
        printf("%d",j+1);
        gotoxy(27,i);
        printf("%s",bil[j].med_name);
        gotoxy(45,i);
        printf("%f",bil[j].cost);
        gotoxy(62,i);
        printf("%d",bil[j].quantity);
        bil[j].total= (float)bil[j].cost*bil[j].quantity;
        gotoxy(70,i);
        printf("%f",bil[j].total);
        sum=sum+bil[j].total;
        i++;
    }
    gotoxy(55,35);
    printf("Gross Amount :  %f",sum);
    gotoxy(57,36);
    printf("   GST @ 18% :  %f",GST_RATE*sum);
    gotoxy(55,37);
    printf("  NET Amount :  %f",(1+GST_RATE)*sum);
    gotoxy(7,40);
    printf("<<<Press 1 for Main Menu>>>");
    gotoxy(7,41);
    scanf("%d",&n);
    if(n==1)
    {
        main_menu();
    }
    getch();
}

//--------------FOR STOCK ALERT--------------
void stock_alert()
{
    int j, n;
    system("cls");
    gotoxy(34,5);
    printf("ALERT FOR STOCK OF MEDICINE");
    //It will display the medicines that are Less in Stock
    box();
    gotoxy(20,10);
    printf("ID.        MEDICINE NAME.           STOCK");
    for(i=18 ; i<=65 ; i++)
    {
        gotoxy(i,11);
        printf("%c",205);
    }
    i=13;
    //It will display the medicines that are Less in Stock
    for(j=0 ; j<num_Med ; j++)
    {
        if(a[j].quantity<=10)
        {
            gotoxy(19,i);
            printf("0%d",a[j].med_id);
            gotoxy(31,i);
            printf("%s",a[j].medi_name);
            gotoxy(56,i);
            printf("%d",a[j].quantity);
            i=i+1;
        }
    }
    gotoxy(7,40);
    printf("<<<Press 1 for Main Menu>>>");
    gotoxy(7,41);
    printf("<<<Press 2 for Medicine Menu>>>");
    gotoxy(7,42);
    printf("<<<Press 3 to Order new Medicine>>>");
    gotoxy(7,43);
    scanf("%d",&n);
    if(n==1)
    {
        main_menu();
    }
    if(n==2)
    {
        medicine();
    }
    if(n==3);
    {
        med_pur();
    }
}

//--------------ABOUT THE STORE--------------
void about()
{
    int c;
    do
    {
        system("cls");
        gotoxy(9,17);
        printf("KJSCE Medical Store is the modern face of Indias pharmacy retail chain.");
        gotoxy(9,18);
        printf("Over the century, this pharmaceutical chain has been serving the health");
        gotoxy(9,19);
        printf("and other pharmaceutical requirements of more than 80 corporate clients,");
        gotoxy(9,20);
        printf("nursing homes, NGOs, and reputed hospitals by delivering quality pharma ");
        gotoxy(9,21);
        printf("and healthcare products and services.");
        gotoxy(39,23);
        printf("OUR MISSION");
        gotoxy(9,25);
        printf("To ensure the availability of quality pharmaceutical and healthcare ");
        gotoxy(9,26);
        printf("products in a highly customer-focused environment and affordable prices &");
        gotoxy(9,27);
        printf("to make sure that the services will continue to touch several lives with ");
        gotoxy(9,28);
        printf("good health and well being.");
        gotoxy(49,36);
        printf("Dishant Padalia   : 1913077");
        gotoxy(49,37);
        printf("Abhishek Mazumdar : 1913064");
        gotoxy(49,38);
        printf("Rahul Doshi       : 1913078");
        box2();
        gotoxy(7,41);
        printf("<<Press 1 for Main Menu>>");
        gotoxy(7,42);
        scanf("%d",&c);
        switch(c)
        {
        case 1:
            main_menu();
            break;
        default:
            gotoxy(7,39);
            printf("Please enter a valid entry");
        }
    }
    while(c!=1);
}

//-----------DISPLAYING DISTRIBUTOR LIST-----------
void dist_list()
{
    int j,n;
    system("cls");
    gotoxy(38,5);
    printf("DISTRIBUTOR LIST");
    box();
    gotoxy(15,10);
    printf("ID.     SUPPLIER NAME.        PH.NO.       CITY.         EMAIL");
    gotoxy(11,11);
    i=13;
    printf("=======================================================================");
    for(j=0; j<6; j++)
    {
        gotoxy(15,i);
        printf("%s",b[j].dist_id);
        gotoxy(24,i);
        printf("%s",b[j].dist_name);
        gotoxy(45,i);
        printf("%s",b[j].mob_no);
        gotoxy(57,i);
        printf("%s",b[j].city);
        gotoxy(70,i);
        printf("%s",b[j].email);
        i=i+2;
    }
    gotoxy(7,25);
    printf("<<<Press 1 for Main Menu>>> ");
    gotoxy(7,26);
    printf("<<<Press 2 for Distributor Menu>>> ");
    gotoxy(7,27);
    scanf("%d",&n);
    if(n==1)
    {
        main_menu();
    }
    if(n==2)
    {
        distributor();
    }
}

//-----------DISTRIBUTOR ENTRY-----------
void dist_add()
{
    char ch;
    do
    {
        system("cls");
        gotoxy(38,5);
        printf("NEW DISTRIBUTOR");
        box();
        gotoxy(7,10);
        printf("Enter ID No. : ");
        scanf("%s",b[num_Dist].dist_id);
        gotoxy(7,13);
        printf("Enter Distributor Name : ");
        scanf("%s",b[num_Dist].dist_name);
        gotoxy(7,16);
        printf("Enter the Mobile Number : ");
        scanf("%s",b[num_Dist].mob_no);
        gotoxy(7,19);
        printf("Enter the City : ");
        scanf("%s",b[num_Dist].city);
        gotoxy(7,22);
        printf("Enter the Email ID : ");
        scanf("%s",b[num_Dist].email);
        num_Dist++;
        gotoxy(7,27);
        printf("Do you want to add more entries [y/n] : ");
        ch=toupper(getche());
    }
    while(ch=='Y');
}

//-----------DISPLAYING MEDICINE LIST-----------
void med_list()
{
    int j, n;
    system("cls");
    gotoxy(38,5);
    printf("MEDICINE LIST");
    box();
    gotoxy(20,10);
    printf("ID.        MEDICINE NAME.           COST(Rs.)");
    for(i=18 ; i<=65 ; i++)
    {
        gotoxy(i,11);
        printf("%c",205);
    }
    i=13;
    for(j=0 ; j<num_Med ; j++)
    {
        gotoxy(19,i);
        printf("0%d",a[j].med_id);
        gotoxy(31,i);
        printf("%s",a[j].medi_name);
        gotoxy(56,i);
        printf("Rs %f",a[j].cost);
        i=i+1;
    }
    gotoxy(7,40);
    printf("<<<Press 1 for Main Menu>>>");
    gotoxy(7,41);
    printf("<<<Press 2 for Medicine Menu>>>");
    gotoxy(7,42);
    scanf("%d",&n);
    if(n==1)
    {
        main_menu();
    }
    if(n==2)
    {
        medicine();
    }
}

//-----------PURCHASE OF NEW MEDICINE-----------
void med_pur()
{
    int temp_medId, temp_quantity;
    float total, temp_cost;
    char temp_medName[20];
    char ch;
    do
    {
        system("cls");
        gotoxy(38,5);
        printf("MEDICINE PURCHASE");
        box();
        gotoxy(7,10);
        printf("Enter ID No. : ");
        scanf("%d",&temp_medId);
        gotoxy(7,13);
        printf("Enter Medicine Name : ");
        scanf("%s",temp_medName);
        gotoxy(7,16);
        printf("Enter the Cost : ");
        scanf("%f",&temp_cost);
        gotoxy(7,19);
        printf("Enter the Quantity : ");
        scanf("%d",&temp_quantity);
        if(temp_cost>=0 && temp_quantity>0)
        {
            a[num_Med].med_id = temp_medId;
            a[num_Med].quantity = temp_quantity;
            a[num_Med].cost = temp_cost;
            strcpy(a[num_Med].medi_name, temp_medName);
        }
        else
        {
            gotoxy(7,21);
            printf("Please enter a valid value");
            getch();
            med_pur();
            num_Med--;
        }
        total=(float)a[num_Med].cost*a[num_Med].quantity;
        gotoxy(7,22);
        printf("The Total Cost is : %f",total);
        num_Med++;
        gotoxy(7,27);
        printf("Do you want to add more entries [y/n] : ");
        ch=toupper(getche());
    }
    while(ch=='Y');
}

//-----------DISPLAYING MEDICINE STOCK-----------
void med_stock()
{
    int j, n;
    system("cls");
    gotoxy(38,5);
    printf("MEDICINE STOCK");
    box();
    gotoxy(20,10);
    printf("ID.        MEDICINE NAME.           STOCK");
    for(i=18 ; i<=65 ; i++)
    {
        gotoxy(i,11);
        printf("%c",205);
    }
    i=13;
    for(j=0 ; j<num_Med ; j++)
    {
        gotoxy(19,i);
        printf("0%d",a[j].med_id);
        gotoxy(31,i);
        printf("%s",a[j].medi_name);
        gotoxy(56,i);
        printf("%d",a[j].quantity);
        i=i+1;
    }
    gotoxy(7,40);
    printf("<<<Press 1 for Main Menu>>>");
    gotoxy(7,41);
    printf("<<<Press 2 for Medicine Menu>>>");
    gotoxy(7,42);
    scanf("%d",&n);
    if(n==1)
    {
        main_menu();
    }
    if(n==2)
    {
        medicine();
    }
}

//-----------SALE OF MEDICINE FOR CUSTOMER-----------
void med_sale()
{
    int j, n, qty, choice, temp_quantity, temp_n;
    num_Bill=0;
    system("cls");
    gotoxy(35,5);
    printf("MEDICINE SALE");
    box();
    gotoxy(20,10);
    printf("SrNo.      MEDICINE NAME.           COST.");
    i=12;
    for(j=0 ; j<num_Med ; j++)
    {
        gotoxy(20,i);
        printf("%d",j+1);
        gotoxy(32,i);
        printf("%s",a[j].medi_name);
        gotoxy(55,i);
        printf("%f",a[j].cost);
        i++;
    }
    j=0;
    do
    {
        gotoxy(7,35);
        printf("Enter the SrNo. of Medicine to buy : ");
        scanf("%d",&temp_n);
        temp_n=temp_n-1;
        gotoxy(7,37);
        printf("Enter the Qty of Medicine : ");
        scanf("%d",&temp_quantity);
        if(temp_quantity<=0)
        {
            gotoxy(7,39);
            printf("Please enter a valid value");
            getch();
            med_sale();
            num_Bill--;
        }
        if(temp_quantity>a[temp_n].quantity)
        {
            gotoxy(7,39);
            printf("NOT IN STOCK !!");
            getch();
            med_sale();
            num_Bill--;
        }
        else
        {
            n=temp_n;
            qty=temp_quantity;
        }
        strcpy(bil[j].med_name, a[n].medi_name);
        bil[j].quantity = qty;
        bil[j].cost = a[n].cost;
        a[n].quantity = a[n].quantity - qty;
        num_Bill++;
        j++;
        gotoxy(7,40);
        printf("Press 1 to purchase more medicines ");
        gotoxy(7,41);
        printf("Press 2 to go to main menu ");
        gotoxy(7,42);
        scanf("%d",&choice);
        if(choice==2)
        {
            main_menu();
        }
    }
    while(choice==1);
}
