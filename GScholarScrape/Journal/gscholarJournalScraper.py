from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import csv
import re

options = webdriver.ChromeOptions()

# unload any css or images
prefs = {
    'profile.default_content_setting_values': {
        'images': 2,
        'permissions.default.stylesheet': 2,
        'javascript': 1
    }
}
# options.add_experimental_option('prefs', prefs)
# options.add_argument('--headless')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

d = { ' Zhaorong Hu': ['Genomic imprinting was evolutionarily conserved during wheat polyploidization (vol 30, pg 37, 2018)',
  'Focus on Chromatin/Epigenetics: GENERAL CONTROL NONREPRESSED PROTEIN5-Mediated Histone Acetylation of FERRIC REDUCTASE DEFECTIVE3 Contributes to Iron Homeostasis in Arabidopsis',
  'Isolation and characterization of Jasmonate induced protein TaJIP in wheat (Triticum aestivum).',
  'Wheat WRKY Gene TaWRKY51 Plays Positive Roles in Drought Stress',
  'Cloning and characterization of the brittle rachis locus Br-A in diploid wheat implicate the history of wheat domestication'],
 ' Jun Wei': ['Implementation of Clean NDN with Network Virtualization',
  'ICNDC 2013',
  'Networking and Distributed Computing',
  'Agent-Aided Software Engineering of High Performance Applications',
  'Evolutionary Scheduling of Dynamic Multitasking Workloads for Elastic Cloud Computing'],
 ' Nicolas Tapon': ['Apical and basal matrix remodeling control epithelial morphogenesis',
  'Structural characterization of the ASPP/PP1 phosphatase complex',
  'The Drosophila AIP orthologue is essential for actin cytoskeleton stabilisation and cell adhesion',
  'Crumbs promotes expanded recognition and degradation by the SCFSˡⁱᵐᵇ/ᵝ⁻ ᵀʳCᴾ ubiquitin ligase',
  'Structural characterization of the ASPP/PP1 phosphatase complex'],
 ' Sabina Moser Tralamazza': ['Streptomyces spp. Isolated from Marine and Caatinga Biomes in Brazil for the Biological Control of Duponchelia fovealis',
  'Histone H3K27 Methylation Perturbs Transcriptional Robustness and Underpins Dispensability of Highly Conserved Genes in Fungi',
  'Multi-Method Approach for Characterizing the Interaction between Fusarium verticillioides and Bacillus thuringiensis Subsp. Kurstaki (vol 10, e0141522, 2015)',
  'IV Simpósio em Microbiologia Aplicada',
  'Isolamento e identificação de fungos do café verde de regiões cafeeiras do Estado do Paraná'],
 ' Benedito Corre_a': ['Signatura: BR0800147.',
  'ENVIRONMENT AND HEALTH—PS 1230',
  'Incidência de micoses superficiais em São Paulo, Capital* Artigo original no idioma Português Brasileiro.',
  'Beer industry in Brazil: Economic aspects, characteristics of the raw material and concerns Pivovarský průmysl v Brazílii: Ekonomické aspekty, charakteristika surovin a rizika',
  'Signatura: BR8902652.'],
 ' Maulik R. Kamdar': ['Focused Clinical Search through Query Intent Interpretation and a Healthcare Knowledge Graph',
  'Focused Clinical Query Understanding and Retrieval of Medical Snippets powered through a Healthcare Knowledge Graph',
  'ReVeaLD: A user-driven domain-specific interactive search platform for biomedical research',
  'Bridging the Usability–Expressivity Gap in Biomedical Data Discovery',
  'Bioinformatics Search'],
 ' Mrinal K. Maiti': ['Characterization of mitochondrial atp6 gene in WA [wild abortive] cytoplasmic male sterile line of rice',
  'Characterization of Arabidopsis mutants exhibiting defects in microsporogenesis.',
  'Studies on acyl carrier protein ACP of Azospirillum brasilense purification of the protein and molecular cloning of the gene',
  'Enhancement of a-linolenic acid content in transgenic tobacco seeds by targeting a plastidial x-3 fatty acid desaturase (fad7) gene of Sesamum indicum to ER',
  'Attempt to modify the fatty acid composition of Brassica seed oil through genetic engineering'],
 ' Yafei Zhang': ['The Element of Nonlinear Optics The Element of Nonlinear Optics 5, 1990',
  'J. Computation Chem. J. Computation Chem. 12, 487, 1991',
  'Supporting Information Hierarchical Heterostructures based on Prickly Ni Nanowires/Cu2O Nanoparticles with Enhanced Photocatalytic Activity',
  'Convolutional neural networks for P300 detection with application to brain-computer interfaces.',
  'Semiconductor and Organic Lasers and Amplifiers Photoelectrochemical Liftoff of Patterned Sapphire Substrate for Fabricating Vertical Light-Emitting Diode..........'],
 ' Sungwon Park': ['Nano-SiC added Ag paste sintering die-attach for SiC power devices',
  'Pressure-less plasma sintering of Cu paste for SiC die-attach of high-temperature power device manufacturing',
  'Partial transient liquid phase bonding for high-temperature power electronics using Sn/Zn/Sn sandwich structure solder',
  'Oxidation resistance and joining properties of Cr-doped Zn bonding for SiC die-attachment',
  'SiC die-attachment with minor elements added pure Zn under formic acid reflow'],
 ' Xiaofei Cong': ['Trim72/cav1 Interaction Determines Repair Influx And Fibrogenesis Outflux In Pulmonary Fibrosis',
  'Trim72 Regulates Complement Phagocytosis In Alveolar Macrophage Via Facultative Inhibition Of Crig',
  'Role of SH3 and Cysteine-Rich Domain 3 (STAC3) in Skeletal Muscle Development, Postnatal Growth and Contraction',
  'TRIM72 regulates complement phagocytosis in alveolar macrophage via facultative recycling of CRIg.',
  'Defective EC coupling is partially responsible for impaired contractibility in hindlimb muscle of Stac3 knockout mice'],
 ' Lian-Wang Guo': ['METABOLISM AND BIOENERGETICS-Electron Transfer from the Rieske Iron-Sulfur Protein (ISP) to Cytochrome f in Vitro. IS A GUIDED TRAJECTORY OF THE ISP NECESSARY FOR COMPETENT …',
  'A guided trajectory for the soluble domain of the Rieske 2fe-2s protein is necessary for competent electron transfer',
  'Effect of salt stress on photosystem Ⅱ heterogeneity in wheat leaves',
  'Photoinhibition of photosynthesis in sweet Viburnum leaves under natural conditions',
  '984–The Spatiotemporal Dynamics of Low-Abundance Bioactive Lipids in Arteries Undergoing Restenosis Observed and Identified at High Spatial Resolving Power with Multi-Modal …'],
 ' Bowen Wang': ['Biomimetic, ROS-detonable nanoclusters—A multimodal nanoplatform for anti-restenotic therapy',
  'Biomimetic vesicles and uses thereof',
  'The Spatiotemporal Dynamics of Low-abundance Bioactive Lipids in Arteries Undergoing Restenosis Observed and Identified at High Spatial Resolving Power with Multi-modal Mass …',
  'Partnership between epigenetic reader BRD4 and transcription factor CEBPD',
  'A non-canonical role and regulations of polo-like kinase-4 in fibroblast cell-type transition'],
 ' Stephen Seedial': ['Transforming Growth Factor β/Smad3 Stimulates Smooth Muscle Cell Migration and Proliferation Through a Signaling Pathway that Involves CXC Chemokine Receptor Type 4 Expression …',
  'Transforming Growth Factor-Beta and its Signaling Mediator Smad3 Enhance Cell Survival After Vascular Injury',
  'TGF-beta/Smad3-treated smooth muscle cells enhance the production of collagen type 3 from adventitial fibroblasts',
  'Accelerated Aneurysmal Dilatation Associated with Apoptosis and Inflammation in a Newly Created Modified Calcium Chloride Rodent AAA Model',
  'Three Dimensional Volumetric Assessment of Orbital Fracture Size: A Novel Technique']}

try:
    with open('gscholarJornalOUT.csv', 'r', encoding='utf8') as f:
        f.read()
except FileNotFoundError:
    with open('gscholarJornalOUT.csv', 'w', newline='', encoding='utf8') as f:
        writer = csv.writer(f)
        writer.writerow(['author',
                         'title',
                         'publish_place'
                         ])
flag = 0
for author in d:
    for title in d[author]:
        try:
            driver.get('https://scholar.google.com.au/')
            driver.find_element(By.XPATH, '//*[@id="gs_hdr_tsi"]').send_keys(title)
            driver.find_element(By.XPATH, '//*[@id="gs_hdr_tsb"]/span/span[1]').click()

            if not flag:
                sleep(20)
                flag = 1

            try:
                # click "cite"
                driver.find_element(By.XPATH, '/html/body/div[1]/div[10]/div[2]/div[3]/div[2]/div[1]/div[2]/div[3]/a[2]/span').click()
                sleep(2)
                publish_place = driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/div[2]/div/div[1]/table/tbody/tr[1]/td/div')
                publish_place = publish_place.find_element(By.XPATH, './/i').text
            except NoSuchElementException:
                publish_place = 'N/A'

            print('author:', author)
            print('title:', title)
            print('publish_place:', publish_place)

            with open('gscholarJornalOUT.csv', 'a', newline='', encoding='utf8') as f:
                writer = csv.writer(f)
                writer.writerow([author,
                                 title,
                                 publish_place])

            print('===================================')

        except NoSuchElementException:
            print("Please do the reCaptcha then enter anything to continue")
            n = input()



