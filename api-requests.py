import aiohttp
import asyncio
import time
import matplotlib.pyplot as plt
import seaborn as sns


time_exp = time.time() + 60


class API_Requests:
    def __init__(self):
        self.num_req = 30
        self.repeticoes_min = 1
        self.tasks = []
        self.time_each_req = []
        self.req_times = []
        self.num_req_list = [] 

    async def get_pokemon(self, session, url):
        async with session.get(url) as resp:
            pokemon = await resp.json()
            return pokemon['name']

    def start(self):       
        async def main():
            async with aiohttp.ClientSession() as session:
                k = self.num_req 
                # Organizar 30 solicitações, aguarda terminar e armazenar o tempo p cada uma delas e depois + 30      
                while time.time() < time_exp:
                    for i in range(self.repeticoes_min):
                        
                        for number in range(1, self.num_req + 1):
                            start_time = time.time() #*1000                            
                            url = f'https://pokeapi.co/api/v2/pokemon/{number}'
                            self.tasks.append(asyncio.ensure_future(self.get_pokemon(session, url)))
                        elements_list = await asyncio.gather(*self.tasks)
                        #print(k)
                        #if k:    
                        end_req_time = time.time() #*1000 
                        req_time = (end_req_time - start_time) #
                        self.req_times.append(req_time)             
                        self.num_req_list.append(len(elements_list))
                        #print('Quantidade requisicoes {} e tempo gasto {}s'.format(k, req_time))
                
                           
                print('\n', self.req_times)
                print('\n', self.num_req_list)
                print('\nForam enviadas {} solicitações a uma taxa de {} solicitações/segundo e o tempo médio de resposta é: {}'.format(len(elements_list), len(elements_list)/60, sum(self.req_times)/len(self.req_times)))


        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        asyncio.run(main())
    

    '''def graficos(self, req_times, elements_list):
        sns.set_theme(style="darkgrid")
        x = self.req_times
        y = self.elements_list
        sns.lineplot(x, y)
        return plt.show()'''
    

api = API_Requests()
api.start()


