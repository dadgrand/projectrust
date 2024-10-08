# prompts.py



questions = [
        "1. Как вам удобно чтобы я вас называл?",
        "2. Вы хотите чтобы я просто структурировал ваши планы или предлагал различные житейские техники?",
        "3. Ваш Возраст?",
        "4. Ваш Пол?",
        "5. Ваш Вес?",
        "6. Ваш Рост?",
        "7. Любимые виды спорта?",
        "8. Вы занимаетесь спортом, ходите в зал?",
        "9. Сколько бы часов в неделю вы готовы тратить на спорт/зал?",
        "10. У вас есть какие-то травмы?",
        "11. Сколько раз в день вы едите? У вас есть диетические предпочтения? Что вы не едите?",
        "12. Во сколько вы просыпаетесь? Хотите ли просыпаться раньше?",
        "13. Во сколько засыпаете? Хотите засыпать раньше?",
        "14. Как бы вы оценили качество сна?",
        "15. Напишите свое учебное/рабочее расписание",
        "16. Сколько вы хотите зарабатывать в месяц?",
        "17. Отметьте сферы жизни в которых вы бы хотели быть лучше",
        "18. Что вас мотивирует?",
        "19. Ваше лучшее качество?",
        "20. Ваше худшее качество?",
        "21. Вы любите шоппинг?",
        "22. Вы бы хотели меньше тратить?",
        "23. Как бы вы оценили свой скилл тайм-менеджмента?",
        "24. Оцените по 10 бальной, насколько вы прокрастинатор?",
        "25. Сколько времени в день вы тратите на социальные сети?",
        "26. Сколько у вас часов экранного времени в день?",
        "27. Вы бы хотели сидеть меньше в телефоне и соц. сетях?",
        "28. Какие у вас хобби и интересы?",
        "29. Как вы любите учить информацию - читать, смотреть, слушать, делать?",
        "30. Сколько часов в неделю вы бы уделяли вещам которые сейчас не делаете но хотели бы делать? Определите по часам каждую - Хобби, изучения новых знаний, овладеваете новыми полезными привычками?",
        "31. Как вы справляетесь со стрессом?",
        "32. Сколько времени вы проводите с семьей и друзьями в день и неделю?",
        "33. Вы бы хотели проводить больше социального времени с ними?",
        "34. Со сколькью людьми вы общаетесь в день, неделю, месяц?",
        "35. Вы бы хотели общаться с большим количеством знакомых людей?",
        "36. Вы бы хотели общаться с большим количеством незнакомых вам людей?",
        "37. Вы знаете какие-то дыхательные техники? Используете их? Хотите чтобы я их советовал?",
        "38. Вы верите в высшие силы? Потустороннию энергию? Следуете какой-то религии?",
        "39. Вы бы хотели получать мотивационные уведомления от меня?",
        "40. Насколько сильно вы готовы отдаться процессу становления новой версии себя? По сто бальной шкале.",
        "41. Насколько детально вы бы хотели чтобы я вам помогал составлять расписание вашего дня? Поминутно, по-получасово, почасово, ещё как то?",
        "42. Каким языком вы хотели бы чтобы я с вами общался? Вежливо, настойчиво, как реальный робот лол, по-дружески, с приколом?",
        "43. Вы готовы проходить опросник каждый вечер, для детализации и улучшения программы?",
        "44. Вы хотите получать итоги недели, месяца, года чтобы видеть свой прогресс?",
        "45. Вы не против участвовать в прямых эфирах - разборах с наставником? (Рандомно выбирается кто-то из зрителей) Пожалуйста, будьте честны по поводу прожитых дней.",
        "46. Вы хотите вести ежедневник? Поверьте, это чит код.",
        "47. Вы готовы брать ответственность за свою жизнь?",
        "48. Вы точно хотите стать лучше?"
    ]


column_names = [
    "preferred_name", "assistance_preference", "age", "gender", "weight", "height",
    "favorite_sports", "sports_activity", "weekly_sport_hours", "injuries",
    "dietary_preferences", "wakeup_time", "sleep_time", "sleep_quality", "schedule",
    "desired_income", "improvement_areas", "motivation", "best_quality", "worst_quality",
    "shopping_preference", "spending_habits", "time_management_skill", "procrastination_level",
    "daily_social_media_time", "daily_screen_time", "reduce_phone_time", "hobbies_interests",
    "learning_preference", "weekly_desired_activities", "stress_management",
    "family_friends_time", "increase_social_time", "communication_frequency",
    "increase_known_people_communication", "increase_unknown_people_communication",
    "breathing_techniques", "belief_system", "receive_motivational_notifications",
    "self_improvement_commitment", "schedule_detailedness", "communication_style",
    "nightly_survey_participation", "progress_reports", "live_session_participation",
    "journaling_interest", "responsibility", "self_improvement_desire"
]