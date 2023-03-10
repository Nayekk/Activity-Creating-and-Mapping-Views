from django.shortcuts import render
from django.http import HttpResponse



def CCMS_Vision(request):
       return HttpResponse ("In 2030, the Manuel S. Enverga University Foundation is a globally competitive university with high concentrations of talent, excellent teaching environment, rigorous program quality, sufficient resources, and a culture of collaboration.");

def CCMS_Mission(request):
       return HttpResponse ("The University is a private non-stock non-profit non-sectarian educational foundation with a three-fold function - instruction, research, and community service - offering responsive and alternative programs supportive of national development and standards of global excellence.");

def CCMS_Objectives(request):
       return HttpResponse ("After graduation, alumni of MSEUF-CSS program shall: 1. Be employed and demonstrate professionalism, competence and passion in solving contemporary computing problems by developing or utilizing innovate IT solutions. 2. Embark in lifelong learning or research to attune to the continuous innovation in the IT industry in order to adapt to the changing demands of th global market; and 3. Exhibit leadership and teamwork, and commitment to their respective local or global organizations.");
       

