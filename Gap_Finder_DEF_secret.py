if isinstance(st.session_state['news'], pd.DataFrame):
                           # ACCUMULATORE PER EVITARE GLI SPAZI VERTICALI NELLE NEWS (STRINGHE PIATTE SENZA ANDARE A CAPO)
                           news_html = ""
                           for a, b in st.session_state['news'].iterrows():
                               ora = datetime.now().hour
                               
                               if ora <= 6:
                                    formatted_date = b['Date'] - timedelta(days=1)
                                    data_ora = datetime.now() - timedelta(days=1)
                               else:
                                    formatted_date = b['Date']
                                    data_ora = datetime.now()
                                    
                               if formatted_date.date() != data_ora.date() and a > 0:
                                    print(formatted_date, data_ora)
                                    break     
                                    
                               data_da_stampa = formatted_date.strftime("%Y-%m-%d | h %H:%M")    
                        
                               link = b['Link']
                               if not link.startswith('http'):
                                    link = "https://finviz.com/" + b['Link']
                                        
                               # Scritto come stringa piatta su un'unica riga per impedire la generazione di box grigi
                               news_html += f'<div style="text-align:left; font-size:13px; margin-bottom:6px; line-height:1.3;"><strong style="color:red;">{data_da_stampa}</strong>&nbsp;<a href="{link}" style="text-decoration:none; color:inherit;" target="_blank">{b["Title"]}</a></div>'
                           
                           # Stampato unicamente una volta fuori dal loop attraverso st.markdown pulito
                           st.markdown(news_html, unsafe_allow_html=True)

                   if isinstance(st.session_state['news'], str):
                           # Usato st.markdown con stringa piatta
                           news_str_html = f'<div style="text-align:center; font-size:14px;">{st.session_state["news"]}</div>'
                           st.markdown(news_str_html, unsafe_allow_html=True)
