from django.urls import path

from sdp import views

urlpatterns =[

    path('',views.loginpg,name='loginpg'),
    path('logout',views.logout,name='logout'),
    path('login_post',views.login_post,name='login_post'),
    path('admin_home',views.admin_home,name='admin_home'),
    path('add',views.add,name='add'),
    path('add_hr',views.add_hr,name='add_hr'),
    path('edit_hr/<int:id>',views.edit_hr,name='edit_hr'),
    path('edithr',views.edithr,name='edithr'),
    path('delete_hr/<int:id>',views.delete_hr,name='delete_hr'),
    path('reply/<int:id>',views.reply,name='reply'),

    path('manage_hr',views.manage_hr,name='manage_hr'),
    path('notification',views.notification,name='notification'),
    path('notificationsend',views.notificationsend,name='notificationsend'),
    path('result',views.result,name='result'),
    path('viewcomplaints',views.viewcomplaints,name='viewcomplaints'),
    path('viewperformance',views.viewperformance,name='viewperformance'),
    path('viewworkstatus',views.viewworkstatus,name='viewworkstatus'),
    path('manage_hr_search',views.manage_hr_search,name='manage_hr_search'),
    path('add_reply',views.add_reply,name='add_reply'),
#________________________HR______________________________________________________________


    path('home', views.home, name='home'),
    path('manage_tl', views.manage_tl, name='manage_tl'),
    path('work_assign_to_tl', views.work_assign_to_tl, name='work_assign_to_tl'),
    path('work_assign_to_tl_search', views.work_assign_to_tl_search, name='work_assign_to_tl_search'),
    path('delete_work/<int:id>', views.delete_work, name='delete_work'),
    path('notification1', views.notification1, name='notification1'),
    path('add1', views.add1, name='add1'),
    path('add_tl', views.add_tl, name='add_tl'),
    path('edit_tl/<int:id>', views.edit_tl, name='edit_tl'),
    path('block_tl/<int:id>', views.block_tl, name='block_tl'),
    path('unblock_tl/<int:id>', views.unblock_tl, name='unblock_tl'),
    path('edittl', views.edittl, name='edittl'),
    path('block_unblock', views.block_unblock, name='block_unblock'),
    path('delete_tl/<int:id>', views.delete_tl, name='delete_tl'),
    path('manage_tl_search',views.manage_tl_search,name='manage_tl_search'),
    path('addwork', views.addwork, name='addwork'),
    path('add_work', views.add_work, name='add_work'),
    path('viewperformance1', views.viewperformance1, name='viewperformance1'),




    #___________TL_________#

path('assign_work_to_tm', views.assign_work_to_tm, name='assign_work_to_tm'),
path('block_unblock1', views.block_unblock1, name='block_unblock1'),
path('Team_Leader', views.Team_Leader, name='Team_Leader'),
path('update_work_status', views.update_work_status, name='update_work_status'),
path('view_doubt_reply', views.view_doubt_reply, name='view_doubt_reply'),
path('view_reportandupd_continous', views.view_reportandupd_continous, name='view_reportandupd_continous'),
path('view_reportandupdate', views.view_reportandupdate, name='view_reportandupdate'),
path('View_teamMember_manage', views.View_teamMember_manage, name='View_teamMember_manage'),
path('View_Work', views.View_Work, name='View_Work'),
path('View_Work', views.View_Work, name='View_Work'),
path('add_tm', views.add_tm, name='add_tm'),
path('add_tm1', views.add_tm1, name='add_tm1'),
path('edit_tm/<id>', views.edit_tm, name='edit_tm'),
path('edittm', views.edittm, name='edittm'),
path('delete_tm/<id>', views.delete_tm, name='delete_tm'),
path('block_tm/<int:id>', views.block_tm, name='block_tm'),
path('unblock_tm/<int:id>', views.unblock_tm, name='unblock_tm'),
path('add_work1', views.add_work1, name='add_work1'),
path('reply1/<int:id>', views.reply1, name='reply1'),
path('add_reply1', views.add_reply1, name='add_reply1'),
path('updateworkstatus', views.updateworkstatus, name='updateworkstatus'),
path('features', views.features, name='features'),
path('featurespost', views.featurespost, name='featurespost'),
path('updatework/<int:id>', views.updatework, name='updatework'),
path('notificationn', views.notificationn, name='notificationn'),












path('and_login', views.and_login, name='and_login'),
path('and_viewmywork', views.and_viewmywork, name='and_viewmywork'),
path('and_viewworkreport', views.and_viewworkreport, name='and_viewworkreport'),
path('and_viewworkreport', views.and_viewworkreport, name='and_viewworkreport'),
path('and_viewnotification', views.and_viewnotification, name='and_viewnotification'),
path('and_viewreply', views.and_viewreply, name='and_viewreply'),
path('and_sendcomplaint', views.and_sendcomplaint, name='and_sendcomplaint'),
path('and_updateworkreport', views.and_updateworkreport, name='and_updateworkreport'),
path('and_prediction', views.and_prediction, name='and_prediction'),




]
