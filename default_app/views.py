from django.shortcuts import render
import json
def index(request):
    return render(request, 'default_app/index.html')

def gallery(request):
    output = []
    for i in range(157):
        qwert = str(i)
        myvar = qwert
        output.append(myvar)
        # output += f'''
        #     <div class="col-lg-4 col-sm-6 mb-4">
        #         <div class="portfolio-item">
        #             <a>
        #                 <div>
        #                     <div class="portfolio-hover-content"></div>
        #                 </div>
        #                 <div class="img-hover">
        #                     <img class="img-fluid myimagebody" src="{myvar}" alt="..." style="object-fit: cover;"/>
        #                 </div>
        #             </a>
        #         </div>
        #     </div>
        # '''

    return render(request, 'default_app/gallery.html', {"output": output})

def terms(request):
    return render(request, 'default_app/tc.html')

def privacy(request):
    return render(request, 'default_app/pp.html')
