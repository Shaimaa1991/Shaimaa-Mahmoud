## Trello Test Plan
**Introduction**

This test plan includes(strategy, techniques, testing level,testing types and Risks) 
Which will give a good coverage and confidence in the trello product.

**References**

Trello system requirements specifications
Trello business requirements specification 
Trello Plan
Configuration Management Plan
Trello structure document

**Test Items**

Trello Mobile application
Trello web application

**Features to be Tested**

We are going to test all below features according to the Trello requirements:
1. Sign up
2. Sign in
3. Forget Password.
4. Create/edit/delete Boards.
5. Create/edit/delete Cards.
6. Notifications.
7. Search.
8. User account settings.

**Features Not to Be Tested**

1. Deactivate and activate Trello account.
2. Trello backups

**Strategy/Approach**

We will apply below techniques
1. Black box.
2.  white box.

We will apply below testing level:
1. Unit testing.
2. Integration testing.
3. regression testing.
4. System testing.
5. UAT testing.

We will apply below testing types:
1. Functional testing.
2. performance testing.
3. usability testing.
4. interrupted testing.

**Item Pass/Fail Criteria**

Each component/feature will be passed only according below:
1. All happy flows are passed.
2. There is no critical or high issue existing.
3. Feature/component does not block any related feature or component.
4. Test coverage is done.
5. all related bugs are fixed and verified. 

**Test Deliverables**

1. Test Plan (this document itself)
2. Test Cases
3. Test Scripts
4. Defect/Enhancement Logs
5. Test Reports
6. Test coverage plan.
7- Maturity rate.

**Test Environment**

We are going to test on below platforms:
1. Android mobiles.
2. iOS mobiles.
3. All web browsers (Chrome, Firefox. Opera, Safari, IE, edge)

**Estimate**

1. This test plan will be applied in 6 weeks each 2 weeks will have a test cycle.
2. 2 testers will assign to this test plan

**Schedule**

1. We have 3 milestones each one will take 2 weeks.
2. We have 6 sprints each one will take a one week.

**Staffing and Training Needs**

Testers will take a technical Training to be able to create the automated tests  

**Responsibilities**

The QC lead and QC manager who are responsible for this test plan.

**Risks**

we may face below risks:
1. Lack of personnel resources when testing is to begin.
2. Lack of availability of required hardware, software, data or tools.
3. Late delivery of the software, hardware or tools.
4. Delays in training on the application and/or tools.
5. Changes to the original requirements or designs.
6. Complexities involved in testing the applications.
7. The test schedule and development schedule will move out an appropriate number of days. 
8. The number of tests performed will be reduced.
9. The number of acceptable defects will be in.
10. The scope of the plan may be changed.

**Approvals**

The CTO should approve on this test plan before we start.

**Version**
v1.0

## High level Scenarios per feature
**Welcome and splash screens**

high level scenario description | Priority 
------------ | -------------
Check that there is a splash screen | 1
Check that there is a 4 slide are displaying as a demo about the trello.| 3
Check that each slide has a different content and each content is meaningful|2
Check that the user can swipe the slides left and righ|2
Check that the welcome screen has the sign up button the sign in button and the slides|1
Check that the in case the user clicks on any copyrights links the application Will navigate to the rights screen|2
Check that in case the user clicks on the sign up button The app will navigate to the sign up screen|1
Check that in case the user clicks on the sign in button The app will navigate to the sign in screen|1


**Sign Up**

high level scenario description | Priority 
------------ | -------------
Check that the below contents are displaying successful: (Fullname, Email, password and signUp button) (links for terms and policy) |1
Check that the user can sign up successful by entering valid data in all mandatory fields
Check that the app will refuse any invalid data in the full name field by  Displaying a meaningful error message in below scenarios:-Try to sign up without entering a full name -Try to sign up by full name less than the minimum length -Try to sign up by full name more than the maximum length -Try to sign up by full name has a special chars or consecutive spaces or digits.|2
Check that the app will refuse any invalid data in the email address field by  Displaying a meaningful error message in below scenarios:  -Try to sign up without entering email address. -Try to sign up by email address more than 256 chars. -Try to sign up by email address less than 6 chars. -Try to sign up by invalid email address (invalid format) -Try to sign up by email address already exist.|2
Check that the app will refuse any invalid data in the password field by  Displaying a meaningful error message in below scenarios:  -Try to sign up without entering a password. -Try to sign up by password less than the maximum length. -Try to sign up by password less than the minimum length -Try to sign up by password does not meet the password criteria.
Try to click on sign up button without entering any data.|2
Check that in case the user clicks on the below links, the app will navigate  to the right screen: -Terms of service. -Privacy policy|3

**Sign In**

high level scenario description | Priority 
------------ | -------------
Check that the user can sign in by clicking on (Sign in with Google) button,  and the app will navigate to another screen to allow the user enter his/her credentials |1
Check that the app can sign in by only his/ her email address only by clicking  On Sign in by SOO button.|1
Check that the user cam sign successful by entering a valid email address and a valid password.|1
Check that the app will refuse any invalid data in the email address and displaying A meaningful email address in bellow scenarios: -Try to sign in without entering email address -Try to sign in by invalid email address -Try to sign in by email address is not registered. |2
Check that the app will refuse any invalid data in the password field by displaying A meaningful error message in all below scenarios: -Try to sign in without entering the password. -Try to sign in by invalid password.|2
Check that the user will refuse sign in by clicking on sign in button without Entering a valid email address and a valid password.|2
Check that the user can reset his/her password by clicking on the forget password button.|1

**Forget Password**

high level scenario description | Priority 
------------ | -------------
Check all content of the forget password are displaying successful.|1
Check that the user can sign in from the forget password screen by clicking login again.|2
Check that the user can reset his password successfully.|1

**Boards**

high level scenario description | Priority 
------------ | -------------
Check that the user can create a new board or card successful |1
Check that all boards are listed in the boards screen |2
Check that the boards screen has a search function| 1
Check that the user can search for board or card successful| 1
Check that when the user search for non existing board or card, system will display no result found to user |3
Check that the user can open the Board successful |1
Try to add more than one board that have the same name | 2
Check that the user can add one or more list on the board succesful |
Try to add more than one board that has the same name | 3
Check that the user can add one or more card on the list | 1
Check that each list has a notification icon and search | 2
Check that the user can add boards public| 2
Check that the user can add boards privite | 2
Check that the user can make a background for the board | 3
Check that the background can be either colors or photos | 3
Check that the user can change the board setting successful | 1
Check that the user can add one or more members to the board | 1
Check that the user can add a description to the board successful | 3
Check that the user can change the power up successful | 2
Check that the power up contains (Calender, Custom fields, Map, Voting)|3
Check that the user can duplicate the board successful | 2
Check that the user can share the board successful | 3
Check that the user can check the board activiaty | 3
Check that the user can synch the activity successful | 3
Check that the user can assign the board to teams and more | 2
Check that the user can add lables to the boards | 2
Check that the user can change and edit the lables | 3
Check that the user can watch and unwatch the board succesful | 3
Check that the user can archive the list or card on the board successful | 2
Check that the user can enable and disbale the comments function on the board successful |2
Check that the user can close and reopen the board successful | 3
Check that the user can minimuize and maximuiez the list size | 3

**Cards**

high level scenario description | Priority 
------------ | -------------
Check that the user can add a new card successful | 1
Check that when the user wants to create a new card the app allows him to select the target board | 2
Check that when the user wants toc reate a new card the app allows him to slect the target list | 2
Check that the can add a card without discription successful | 3
Try to add more than one card that have the same name| 3
Check that the user can select a due date for the cards succesful | 2
Check that the user can set a reminder for the cards succesful |2
Check that the user can assign one or more member to the card successful | 2
Check that the user can add attachments successful to the cards | 2

**Home**

high level scenario description | Priority 
------------ | -------------
Check that the user can add cards , boards and lists from the home screen| 1
Check that the user can check all cards and activities from the home screen | 1
Check that the application has a hint message to the user on the home screen in case there is no activities | 3
Check that the main menu has (Boards, Home, Search , Notifications, Accounts) tabs.| 1

**Search**

high level scenario description | Priority 
------------ | -------------
Check that the user can search for card , list or board successful | 1
Check that in case the user searches for non existing items , system will display no result found to the user | 2
Check that the system keeps all pervious searches on the recent section |3

**Notifications**

high level scenario description | Priority 
------------ | -------------
Check that the user can show all notification in All tab| 1
Check that the user can shwo only "his or her" notification on me tab successful | 1
Check that the user can show only comments on comments tab successful | 1
Check that the user can read and open any notification | 2
Check that the user can mark one or all notifications as read successful | 2
Check that the user can edit notification settings succesful | 1
Check that the user can enable and disable mention notification on the mobile | 2
Check that the user can enable and disable duo soon notification on the mobile | 2
Check Check that the user can enable and disable card notifications such as (added to a card, removed to a card, comment on a card, attachment added to a card, change made to a card, new card created) successful | 2
Check Check that the user can enable and disable boards notifications such as (added to a board, removed to a board, made an administrator of aboard , board has been closed) | 2
Check that the user can enable and disable team notification such as (Added to a team, removed from a team, made an administrator of a team)|2

**User Account**

high level scenario description | Priority 
------------ | -------------
Check that the user can change his/her profile picture successful | 3
Check that the user can upgrade his account to Trello Gold successful |1
Check that the User can log out successful |1
Check that the user can enable and disable color blind mode |3
Check that the user can enable and disable Sync successful |3
Check that the user can open and share sync queue successful | 3
Check that the user can edit the experiments setting successful | 2
Check that the user can reset the the experiments settings successful |2
Check that the user can enable and disable reactions in push notifications successful | 3
Check that the user can enable and disable add card experiments | 3
Check that the user can check his / her information successful| 2
Check that the user can check the digontics reports successful | 3
Check that the user can check the error report and share it | 3
Check that the user can delete his/her account |1
Check that in case the user wants to delete his account system will allow the user to recover his data |1
Check that there is a help function|3
Check that the user can check the privacy of the app successful | 3
Check that the user can read the terms of service successful |3
Check that the user can get all acknowledgments | 3
Check that the user can be a beat tester | 3
Check that the user able to rate the application |2

**Performance high level scenarios**

high level scenario description | Priority 
------------ | -------------
Check the time application takes to start up |1
Check How much battery does it consume |2
Check if the system running in the background is retrieved |2
verify speed and response time of APP under different networks |1
Ensure the application do not get crashed.|1
Ensure the application perform well while using data, Wi-Fi or other connectivity |3
Check if the application get slow if it is used for a long time |2
Check if the application get slow with increase in size of the local database | 2
Check how well does it work with slow network connections |2
Have few applications open in background and then try to run the application |2
Try to turn on the screen rotation and rotate the screen and instantly click on some functionalities and check if they behave they way it is expected or not |1
check the behavior of the application when the phone is offline from data.|2

**Interrupted tests high level scenarios**

high level scenario description | Priority 
------------ | -------------
Check application behavior when Battery low alert is shown |3
Check application behavior when Battery full- when charging |3
Check application behavior while Incoming phone call|2
Check application behavior while Incoming SMS|2
Check application behavior while Incoming Alert from another mobile application|2
Check application behavior while Plugged in for charging |2
Check application behavior while Plugged out from charging|2
Check application behavior while Device shut off |2
Check application behavior while Application Update reminders are shown | 2
Check application behavior while Alarm ringing |2
Check application behavior when Network connection lost |1
Check application behavior when Network connection restored |1
Check application behavior while Getting a message on WhatsApp or other similar message apps|2
Check application behavior when Phone auto-locked |3
Check application behavior while Putting the application into the background and back to it |2

**Usability tests high level scenarios**

high level scenario description | Priority 
------------ | -------------
Check that system displays validation error messages at the correct position, and error messages are comprehensive and readable | 2
Check that all error messages are displayed with same style |3
Check that all general confirmation messages are using same style, which differes than error messages style |2
Check that fields tips/hints are meaningful and positioned correctly on the screen |3
Check that all pages doesn't have grammatical or spelling error |3
Check that all fields in every page are aligned properly | 3
Check that all screen titles are meaningful and clearly represent the page contents |2
Check that the application is user-friendly and doesn't have blocking scenarios for various first user experience |1






