from locators import Locators

tabs = [
        Locators.text_sauces,
        Locators.text_rools,
        Locators.text_fillings
    ]

     #Сопоставляем табы с их активными классами
tab_to_active_class = {
        Locators.text_sauces: Locators.sauces_active,
       Locators.text_rools: Locators.rolls_active,  
        Locators.text_fillings: Locators.fillings_active
    }
    # Сопоставляем табы с их активными классами
