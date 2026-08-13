const entries = [
  // --- Science ---
  {
    title: "Theory of Relativity",
    category: "Science",
    status: "Scientific Theory",
    description: "Albert Einstein's revolutionary framework describing space, time, and gravity through Special and General Relativity.",
    explanation: "Special Relativity shows that space and time are linked for objects moving at consistent speeds, introducing time dilation. General Relativity explains gravity not as a force, but as the bending of spacetime caused by mass and energy.",
    whyInteresting: "It completely redefined our understanding of gravity, showed that time is relative, and predicted black holes and gravitational waves decades before they were observed.",
    tags: ["physics", "gravity", "einstein", "space-time"],
    related: ["Quantum Mechanics", "Big Bang Theory"],
    contentIdeas: [
      "How Einstein ruined our intuitive understanding of time",
      "The physics of interstellar travel: Time dilation explained",
      "Why gravity isn't actually a force"
    ]
  },
  {
    title: "Evolution by Natural Selection",
    category: "Science",
    status: "Scientific Theory",
    description: "Charles Darwin's theory explaining how organisms adapt and evolve over generations through the survival and reproduction of individuals with favorable traits.",
    explanation: "Within any population, individuals possess varying traits. Those with traits better suited to their environment are more likely to survive, reproduce, and pass those traits on, gradually modifying the species over vast timescales.",
    whyInteresting: "It provides a single, elegant mechanism that explains the staggering diversity, complexity, and interconnectedness of all life on Earth.",
    tags: ["biology", "evolution", "darwin", "genetics"],
    related: ["Simulation Hypothesis", "Dunning-Kruger Effect"],
    contentIdeas: [
      "The beautiful simplicity of Darwin's great idea",
      "Are humans still evolving? The future of natural selection",
      "The most extreme examples of evolutionary adaptation"
    ]
  },
  {
    title: "Big Bang Theory",
    category: "Science",
    status: "Scientific Theory",
    description: "The prevailing cosmological model explaining the origin and early expansion of the universe from an extremely hot, dense point.",
    explanation: "Approximately 13.8 billion years ago, the universe rapidly expanded from an infinitely dense singularity. As it cooled, subatomic particles, atoms, stars, and galaxies formed, a process that continues today as the universe expands.",
    whyInteresting: "It places a definitive beginning on time and space as we know them and allows us to trace the history of the entire universe back to its first fractions of a second.",
    tags: ["cosmology", "universe", "origins", "physics"],
    related: ["Theory of Relativity", "Quantum Mechanics", "Boltzmann Brain"],
    contentIdeas: [
      "What actually happened at the very beginning of time?",
      "How scientists mapped the echo of the Big Bang",
      "What was there before the universe began?"
    ]
  },
  {
    title: "Quantum Mechanics",
    category: "Science",
    status: "Scientific Theory",
    description: "The branch of physics dealing with the strange behavior of matter and light at atomic and subatomic scales.",
    explanation: "At the quantum level, particles can exist in multiple states at once (superposition), influence each other instantly across distances (entanglement), and act as both waves and particles.",
    whyInteresting: "It challenges the deterministic nature of classical physics, proving that at the most fundamental level, reality is ruled by probability and observer-dependent phenomena.",
    tags: ["quantum", "subatomic", "physics", "probability"],
    related: ["Theory of Relativity", "Simulation Hypothesis", "Boltzmann Brain"],
    contentIdeas: [
      "Why quantum physics is weirder than science fiction",
      "Einstein's nightmare: Quantum entanglement explained simply",
      "Is reality only real when we look at it?"
    ]
  },
  {
    title: "Simulation Hypothesis",
    category: "Science",
    status: "Hypothesis",
    description: "The proposal that our reality is an extremely advanced artificial simulation, likely run by a post-human or highly evolved civilization.",
    explanation: "As computing power grows exponentially, it is theoretically possible to simulate entire universes. If thousands of simulated realities exist but only one real one, statistically we are highly likely to be inside a simulation.",
    whyInteresting: "It bridges the gap between physics, philosophy, and computation, offering a modern, digital alternative to classic metaphysical questions about the nature of existence.",
    tags: ["metaphysics", "reality", "computation", "philosophy"],
    related: ["Brain in a Vat", "Quantum Mechanics", "Boltzmann Brain"],
    contentIdeas: [
      "Are we living in a video game? The simulation theory explained",
      "The scientific glitches that suggest reality is simulated",
      "If life is a simulation, who is running the computer?"
    ]
  },
  // --- Philosophy ---
  {
    title: "Ship of Theseus",
    category: "Philosophy",
    status: "Philosophical Idea",
    description: "A classic thought experiment exploring whether an object that has had all of its parts replaced remains fundamentally the same object.",
    explanation: "If a ship's wooden planks are gradually replaced one by one until not a single original piece remains, is it still the same ship? If the old planks are gathered and assembled into a new ship, which one is the original?",
    whyInteresting: "It exposes deep contradictions in how we define identity, persistence, and self, extending directly to questions about human cells and personal identity.",
    tags: ["identity", "paradox", "metaphysics", "thought-experiment"],
    related: ["Brain in a Vat", "Problem of Other Minds"],
    contentIdeas: [
      "If you replace every cell in your body, are you still you?",
      "The Ship of Theseus: A ancient paradox that breaks logic",
      "Who owns the original? The philosophy of identity"
    ]
  },
  {
    title: "Brain in a Vat",
    category: "Philosophy",
    status: "Philosophical Idea",
    description: "A skepticism thought experiment imagining a brain kept alive in a jar, receiving simulated electrical impulses that mimic reality.",
    explanation: "If a mad scientist could stimulate your isolated brain to perceive walking, tasting, and seeing exactly as you do now, you would have no logical way of proving that your physical body is real and active.",
    whyInteresting: "It highlights the ultimate limitations of empirical knowledge and human sensory perception, forming the foundation of modern epistemological skepticism.",
    tags: ["skepticism", "perception", "epistemology", "mind"],
    related: ["Simulation Hypothesis", "Problem of Other Minds", "Boltzmann Brain"],
    contentIdeas: [
      "How do you prove your life isn't a dream in a jar?",
      "The Brain in a Vat: The ultimate philosophical nightmare",
      "René Descartes and the origin of simulated doubts"
    ]
  },
  {
    title: "Boltzmann Brain",
    category: "Philosophy",
    status: "Philosophical Idea",
    description: "A cosmological thought experiment suggesting that it is statistically more likely for a single brain to spontaneously fluctuate into existence in a void than for our entire universe to evolve.",
    explanation: "Over infinite time, thermodynamic fluctuations will randomly assemble particles. The odds of creating a single conscious brain with memories of an imaginary life are astronomically higher than the odds of creating our entire ordered cosmos.",
    whyInteresting: "It is a reductio ad absurdum argument used by physicists to point out deep flaws in existing cosmological models and theories of entropy.",
    tags: ["cosmology", "entropy", "mind", "probability"],
    related: ["Big Bang Theory", "Quantum Mechanics", "Simulation Hypothesis"],
    contentIdeas: [
      "The Boltzmann Brain: The most terrifying concept in cosmology",
      "Are you a real person or a random glitch in a void?",
      "Why physicists are scared of thermodynamic fluctuations"
    ]
  },
  {
    title: "Problem of Other Minds",
    category: "Philosophy",
    status: "Philosophical Idea",
    description: "The philosophical challenge of proving that other people possess conscious minds and experiences similar to our own.",
    explanation: "We can easily observe the behavior and physical reactions of others, but we can never directly experience their consciousness. Therefore, it is impossible to conclusively prove that others are not mindless automatons or philosophical zombies.",
    whyInteresting: "It highlights the absolute isolation of subjective experience, forcing us to question the boundary between empathy, observation, and pure assumption.",
    tags: ["consciousness", "mind", "solipsism", "skepticism"],
    related: ["Brain in a Vat", "Ship of Theseus"],
    contentIdeas: [
      "How do you know everyone else isn't a robot?",
      "The mystery of the Philosophical Zombie",
      "Solipsism: Is it possible that only you exist?"
    ]
  },
  {
    title: "Infinite Regress",
    category: "Philosophy",
    status: "Philosophical Idea",
    description: "A logical paradox where any proposition requires a justification, which itself requires a justification, continuing forever without end.",
    explanation: "If every statement needs proof, then the proof needs proof, creating an endless chain. In physics, this is often expressed as 'turtles all the way down' when asking what supports the structure of reality.",
    whyInteresting: "It exposes the fragility of human logic and knowledge, showing that all belief systems must eventually rest on unproven assumptions or circular logic.",
    tags: ["logic", "paradox", "knowledge", "reason"],
    related: ["Boltzmann Brain", "Problem of Other Minds"],
    contentIdeas: [
      "The logic loop that proves we know nothing for sure",
      "Turtles all the way down: Understanding infinite regress",
      "How to break the endless loop of 'Why?'"
    ]
  },
  // --- Psychology ---
  {
    title: "Dunning-Kruger Effect",
    category: "Psychology",
    status: "Hypothesis",
    description: "A cognitive bias where people with limited competence in a domain overestimate their own abilities, while experts tend to underestimate theirs.",
    explanation: "Inexperienced individuals lack the exact skill needed to recognize their own deficiencies. Conversely, highly skilled individuals often assume that tasks easy for them are equally easy for everyone else.",
    whyInteresting: "It explains why confidence and competence are so frequently mismatched in public debates, workplaces, and daily life, though researchers debate its exact statistical nature.",
    tags: ["cognitive-bias", "mind", "behavior", "competence"],
    related: ["Confirmation Bias", "Cognitive Dissonance"],
    contentIdeas: [
      "Why incompetent people think they're amazing",
      "The psychology of confidence: Understanding Dunning-Kruger",
      "How to spot the bias in your own thinking"
    ]
  },
  {
    title: "Bystander Effect",
    category: "Psychology",
    status: "Established",
    description: "A social psychological phenomenon where individuals are less likely to offer help to a victim when other people are present.",
    explanation: "When others are around, responsibility is diffused across the crowd. Individuals assume someone else has already called for help or will step in, combined with social cues from surrounding passive observers.",
    whyInteresting: "It challenges our beliefs about human morality and altruism, proving that group dynamics can override individual empathy in critical situations.",
    tags: ["social-psychology", "behavior", "empathy", "groups"],
    related: ["Diffusion of Responsibility", "Collective Behavior"],
    contentIdeas: [
      "Why crowds ignore emergencies: The Bystander Effect",
      "The shocking psychology behind the tragedy of Kitty Genovese",
      "How to force a crowd to help you in an emergency"
    ]
  },
  {
    title: "Confirmation Bias",
    category: "Psychology",
    status: "Established",
    description: "The universal tendency to search for, interpret, favor, and recall information in a way that confirms one's preexisting beliefs or hypotheses.",
    explanation: "Our brains prefer cognitive comfort. When encountering new evidence, we filter out facts that challenge us and overemphasize facts that support us, creating echo chambers of belief.",
    whyInteresting: "It is the root cause of many superstitious beliefs, political polarization, and scientific errors, acting as a constant barrier to objective thinking.",
    tags: ["cognitive-bias", "irrationality", "beliefs", "mind"],
    related: ["Dunning-Kruger Effect", "Cognitive Dissonance"],
    contentIdeas: [
      "Why we only see what we want to believe",
      "How confirmation bias controls your social media feed",
      "The scientific method: Our only shield against ourselves"
    ]
  },
  {
    title: "Cognitive Dissonance",
    category: "Psychology",
    status: "Established",
    description: "The mental discomfort experienced by someone who holds two or more contradictory beliefs, ideas, or values at the same time.",
    explanation: "When behavior conflicts with beliefs, it creates psychological tension. To relieve this, people will rationalize their actions, change their beliefs, or deny evidence that threatens their identity.",
    whyInteresting: "It reveals that human reasoning is often used to justify our behavior after the fact, rather than to make rational decisions beforehand.",
    tags: ["social-psychology", "mind", "tension", "rationalization"],
    related: ["Confirmation Bias", "Dunning-Kruger Effect"],
    contentIdeas: [
      "The mental gymnastics we do to justify our mistakes",
      "What happens to your brain when your beliefs are shattered?",
      "Cognitive dissonance: The silent conflict in your mind"
    ]
  },
  {
    title: "Mandela Effect",
    category: "Psychology",
    status: "Hypothesis",
    description: "A phenomenon where a large group of people share a collective false memory of an event or detail.",
    explanation: "Named after Nelson Mandela, whom many falsely remembered dying in prison in the 1980s. Psychologists attribute it to memory confabulation, suggestibility, and social reinforcement, while others speculate about parallel universes.",
    whyInteresting: "It demonstrates how fragile and reconstructive human memory is, showing that a memory can feel completely real to millions of people despite being factually incorrect.",
    tags: ["memory", "perception", "society", "illusion"],
    related: ["Bystander Effect", "Simulation Hypothesis"],
    contentIdeas: [
      "Why millions of people remember a history that never happened",
      "The Mandela Effect: Proof of parallel universes or bad memories?",
      "The most famous false memories you probably still believe"
    ]
  },
  // --- Society ---
  {
    title: "Game Theory",
    category: "Society",
    status: "Established",
    description: "The mathematical framework for analyzing strategic interactions between rational decision-makers.",
    explanation: "It models scenarios where the outcome for each participant depends on the choices of all. It analyzes concepts like the Prisoner's Dilemma, showing why cooperative strategies can fail even when they are mutually beneficial.",
    whyInteresting: "It explains human behavior in economics, international politics, evolution, and daily social conflicts using precise mathematical rules.",
    tags: ["mathematics", "cooperation", "economics", "strategy"],
    related: ["Social Contract Theory", "Rational Choice Theory"],
    contentIdeas: [
      "The mathematics of betrayal: Game Theory explained",
      "Why rational people make terrible group choices",
      "How Game Theory kept the Cold War from turning hot"
    ]
  },
  {
    title: "Social Contract Theory",
    category: "Society",
    status: "Philosophical Idea",
    description: "The political theory that individuals consent, either explicitly or tacitly, to surrender some freedoms to authority in exchange for protection of their remaining rights.",
    explanation: "Without a ruling body, humans live in a chaotic 'state of nature' ruled by fear. To escape this, we agree to form a society and abide by collective laws, establishing the legitimacy of political power.",
    whyInteresting: "It forms the philosophical basis for modern democratic governments, human rights, and the rule of law.",
    tags: ["politics", "society", "authority", "rights"],
    related: ["Game Theory", "Collective Behavior"],
    contentIdeas: [
      "Why do we obey laws we didn't write?",
      "Thomas Hobbes vs. John Locke: The battle for human nature",
      "What happens when the social contract is broken?"
    ]
  },
  {
    title: "Rational Choice Theory",
    category: "Society",
    status: "Hypothesis",
    description: "A framework assuming that individuals always make logical decisions that provide them with the highest personal utility or benefit.",
    explanation: "This theory models human behavior as a series of calculated cost-benefit analyses. While useful for modeling markets, it is heavily criticized for ignoring emotional, social, and psychological factors in decision-making.",
    whyInteresting: "It highlights the tension between idealized economic models of 'Homo economicus' and the messy, irrational reality of actual human behavior.",
    tags: ["economics", "behavior", "utility", "logic"],
    related: ["Game Theory", "Confirmation Bias"],
    contentIdeas: [
      "Do we actually make rational decisions?",
      "The myth of the perfectly rational human being",
      "Why economics fails to predict human behavior"
    ]
  },
  {
    title: "Diffusion of Responsibility",
    category: "Society",
    status: "Established",
    description: "A socio-psychological effect where people feel less pressure to take action in a group because they assume others will do it.",
    explanation: "As group size increases, the felt responsibility of each individual decreases proportionally. It is the primary psychological driver of the Bystander Effect and organizational inertia.",
    whyInteresting: "It explains why large organizations and societies fail to act on slow-moving crises, like climate change or corporate corruption.",
    tags: ["psychology", "social-groups", "responsibility", "inaction"],
    related: ["Bystander Effect", "Collective Behavior"],
    contentIdeas: [
      "Why nobody takes responsibility in large groups",
      "How corporate hierarchies dilute individual ethics",
      "The danger of assuming 'someone else will fix it'"
    ]
  },
  {
    title: "Collective Behavior",
    category: "Society",
    status: "Established",
    description: "The study of spontaneous, unstructured behaviors that emerge when groups of people react to common stimuli, such as crowds, mobs, and social panics.",
    explanation: "When individuals gather in a crowd, they can experience 'deindividuation'—a loss of self-awareness. Social norms dissolve, and emotions spread rapidly, leading to riots, fads, or mass panics.",
    whyInteresting: "It reveals how quickly civilized human beings can abandon individual reasoning and adapt to the volatile, singular mind of a crowd.",
    tags: ["sociology", "crowds", "panics", "behavior"],
    related: ["Social Contract Theory", "Diffusion of Responsibility"],
    contentIdeas: [
      "The terrifying speed of crowd psychology",
      "How moral panics spread through modern society",
      "The science of why good people join angry mobs"
    ]
  },
  // --- History ---
  {
    title: "Fall of the Roman Empire",
    category: "History",
    status: "Historical Claim",
    description: "The complex process of decline, fragmentation, and collapse of the Western Roman Empire during the 5th century AD.",
    explanation: "Rather than a single catastrophic event, Rome fell due to a combination of barbarian invasions, economic instability, internal corruption, military overreach, and political divisions.",
    whyInteresting: "It serves as the ultimate historical warning, showing how even the most powerful global superpowers can decay from within and collapse.",
    tags: ["rome", "collapse", "empire", "antiquity"],
    related: ["Library of Alexandria", "Social Contract Theory"],
    contentIdeas: [
      "How the world's greatest empire slowly destroyed itself",
      "The real reasons behind the fall of Rome",
      "Are modern superpowers following the path of Rome?"
    ]
  },
  {
    title: "Library of Alexandria",
    category: "History",
    status: "Historical Claim",
    description: "The legendary library of the ancient world in Egypt, symbolizing the height of classical knowledge and its tragic destruction.",
    explanation: "Founded in the 3rd century BC, it housed hundreds of thousands of scrolls. Its destruction is often attributed to a single fire set by Julius Caesar, but it actually suffered a slow decline over centuries due to budget cuts, religious riots, and warfare.",
    whyInteresting: "It acts as a tragic warning about the fragility of human knowledge and historical records in the face of conflict and neglect.",
    tags: ["alexandria", "knowledge", "libraries", "ancient-history"],
    related: ["Fall of the Roman Empire", "Atlantis"],
    contentIdeas: [
      "The true story of the burning of the Library of Alexandria",
      "How much human knowledge was actually lost in Alexandria?",
      "The slow, tragic death of the ancient world's greatest library"
    ]
  },
  {
    title: "Dancing Plague of 1518",
    category: "History",
    status: "Historical Claim",
    description: "A bizarre case of mass psychogenic illness in Strasbourg, France, where hundreds of people danced uncontrollably for days without rest.",
    explanation: "Starting with a single woman, the phenomenon spread to hundreds of citizens. Many danced until they collapsed or died from exhaustion. Historians attribute it to extreme stress-induced mass hysteria or ergot poisoning (hallucinogenic mold on rye).",
    whyInteresting: "It shows how physical symptoms can be triggered entirely by psychological stress and social contagion within a community.",
    tags: ["france", "hysteria", "mystery", "middle-ages"],
    related: ["Collective Behavior", "Bystander Effect"],
    contentIdeas: [
      "The history of the plague that made people dance to death",
      "What caused the Dancing Plague of 1518?",
      "When minds glitch: The mystery of mass psychogenic illness"
    ]
  },
  {
    title: "Lost Colony of Roanoke",
    category: "History",
    status: "Historical Claim",
    description: "The unsolved mystery of an early English settlement in North Carolina whose entire population vanished, leaving only a single word carved into a post.",
    explanation: "In 1590, a supply ship returned to Roanoke Island to find the colony abandoned with no signs of struggle. The word 'CROATOAN' carved into a wooden post suggested they may have integrated with local Native American tribes.",
    whyInteresting: "It is one of America's oldest cold cases, illustrating the extreme dangers of early colonization and the mystery of total abandonment.",
    tags: ["mystery", "colonization", "america", "vanished"],
    related: ["Bermuda Triangle", "Atlantis"],
    contentIdeas: [
      "What really happened to the Lost Colony of Roanoke?",
      "Decoding 'Croatoan': The clues behind Roanoke's disappearance",
      "The theories that solve America's oldest historical mystery"
    ]
  },
  {
    title: "Tunguska Event",
    category: "History",
    status: "Historical Claim",
    description: "A massive, unexplained explosion in a remote Siberian forest in 1908 that flattened over 80 million trees with no impact crater.",
    explanation: "Scientists believe the blast was caused by the airburst of a stony meteoroid or comet fragment disintegrating 5 to 10 kilometers above the surface, releasing energy 1,000 times greater than the atomic bomb dropped on Hiroshima.",
    whyInteresting: "It is the largest impact event on Earth in recorded history, demonstrating the devastating potential of cosmic collisions that leave no physical crater.",
    tags: ["siberia", "explosion", "meteor", "space-impact"],
    related: ["Big Bang Theory", "Bermuda Triangle"],
    contentIdeas: [
      "The day the sky exploded: The Tunguska Event",
      "Why did the largest explosion in history leave no crater?",
      "The terrifying science of cosmic airbursts"
    ]
  },
  // --- Mysteries / Popular Ideas / Conspiracies ---
  {
    title: "Fermi Paradox",
    category: "Mysteries",
    status: "Controversial",
    description: "The apparent contradiction between the high mathematical probability of extraterrestrial civilizations and our total lack of evidence or contact.",
    explanation: "With billions of stars in our galaxy, many older than our sun, intelligent life should have evolved and colonized the stars by now. Yet, we observe absolute silence in the cosmos. Proposed answers range from 'The Great Filter' to the 'Zoo Hypothesis'.",
    whyInteresting: "It forces us to confront either our absolute loneliness in the universe or the terrifying possibility that advanced civilizations are systematically destroyed before they can contact us.",
    tags: ["space", "aliens", "fermi", "existential-risk"],
    related: ["Simulation Hypothesis", "Boltzmann Brain"],
    contentIdeas: [
      "If aliens exist, where is everybody? The Fermi Paradox",
      "The most disturbing solutions to the Fermi Paradox",
      "Are we alone in the universe?"
    ]
  },
  {
    title: "Bermuda Triangle",
    category: "Mysteries",
    status: "Speculative",
    description: "A popular maritime mystery involving a region in the western North Atlantic where numerous aircraft and ships are claimed to have vanished under mysterious circumstances.",
    explanation: "Popular culture attributes these disappearances to magnetic anomalies, wormholes, or Atlantis. However, data from marine insurers and coast guards show that the rate of accidents in this highly traveled area is no higher than in any other part of the ocean.",
    whyInteresting: "It is a prime example of how media sensationalism, confirmation bias, and selective reporting can build a modern mythology out of normal statistical patterns.",
    tags: ["ocean", "myths", "disappearances", "probability"],
    related: ["Confirmation Bias", "Mandela Effect", "Lost Colony of Roanoke"],
    contentIdeas: [
      "The truth behind the Bermuda Triangle disappearances",
      "How the media invented the Bermuda Triangle myth",
      "Why ships actually sink in the Atlantic"
    ]
  },
  {
    title: "Moon Landing Conspiracy",
    category: "Conspiracies",
    status: "Conspiracy Theory",
    description: "The widely debunked belief that the Apollo Moon landings were faked by NASA in a Hollywood studio to win the Space Race.",
    explanation: "Conspiracy theorists point to supposed anomalies in photos, like the lack of stars or the waving flag. Scientists and historians have thoroughly disproven these claims, explaining them through photographic physics, vacuum dynamics, and the sheer impossibility of keeping a 400,000-person conspiracy secret.",
    whyInteresting: "It serves as a case study in how deep distrust of government institutions can feed grand, complex conspiracy theories that reject overwhelming physical evidence.",
    tags: ["conspiracy", "apollo", "space", "debunked"],
    related: ["Illuminati Conspiracy", "Confirmation Bias"],
    contentIdeas: [
      "Why do people believe the Moon landing was fake?",
      "The evidence behind the Apollo Moon landings",
      "How hard would it be to actually fake a moon landing?"
    ]
  },
  {
    title: "Illuminati Conspiracy",
    category: "Conspiracies",
    status: "Conspiracy Theory",
    description: "The conspiracy theory that a secretive global elite controls world events, governments, and economies to establish a totalitarian New World Order.",
    explanation: "While a real historical Bavarian Illuminati existed in the late 18th century advocating for secularism and rationalism, modern theories claim they survived in secret and control global media, finance, and royalty.",
    whyInteresting: "It represents the archetypal grand conspiracy theory, offering a simplified (albeit terrifying) explanation for the chaotic and unpredictable nature of global politics.",
    tags: ["conspiracy", "secret-society", "control", "politics"],
    related: ["Moon Landing Conspiracy", "Social Contract Theory"],
    contentIdeas: [
      "The real history of the Bavarian Illuminati",
      "How secret society myths control the modern imagination",
      "Why our brains love the idea of a secret global elite"
    ]
  },
  {
    title: "Atlantis",
    category: "Myths & Legends",
    status: "Myth / Legend",
    description: "A legendary island civilization first described by Plato as a moral allegory, which has since become a popular symbol of a lost golden age.",
    explanation: "Plato wrote of Atlantis as a powerful naval empire that sank into the ocean in a single day of misfortune after failing to conquer Athens. There is no historical or archaeological evidence that Atlantis existed; it was created as a philosophical allegory of hubris.",
    whyInteresting: "It shows how an ancient philosophical thought experiment was transformed over centuries into a literal historical mystery, inspiring countless searches and pseudoscientific theories.",
    tags: ["plato", "philosophy", "lost-city", "mythology"],
    related: ["Ship of Theseus", "Library of Alexandria", "Bermuda Triangle"],
    contentIdeas: [
      "Did Atlantis ever exist?",
      "The real history behind the Atlantis myth",
      "How Plato's allegory became history's greatest mystery"
    ]
  }
];

// Document elements
const cardsGrid = document.getElementById("cards-grid");
const searchInput = document.getElementById("search-input");
const categoryFiltersContainer = document.getElementById("category-filters");
const detailModal = document.getElementById("detail-modal");
const modalOverlay = document.getElementById("modal-overlay");

// State
let activeCategory = "All";
let searchQuery = "";

// Initialize
function init() {
  renderCategories();
  renderCards();
  setupEventListeners();
}

// Render Category Filter Buttons
function renderCategories() {
  const categories = [
    "All",
    "Science",
    "Philosophy",
    "Psychology",
    "Society",
    "History",
    "Mysteries",
    "Myths & Legends",
    "Conspiracies"
  ];
  
  categoryFiltersContainer.innerHTML = categories.map(cat => {
    const activeClass = cat === activeCategory ? 'active' : '';
    return `<button class="filter-btn ${activeClass}" data-category="${cat}">${cat}</button>`;
  }).join('');
}

// Normalize strings for cleaner search
function cleanString(str) {
  return str.toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "");
}

// Render Cards with current state filters applied
function renderCards() {
  const filtered = entries.filter(entry => {
    // Category match
    const categoryMatch = activeCategory === "All" || entry.category === activeCategory;
    
    // Search query match
    let searchMatch = true;
    if (searchQuery) {
      const q = cleanString(searchQuery);
      const titleClean = cleanString(entry.title);
      const descClean = cleanString(entry.description);
      const catClean = cleanString(entry.category);
      const tagsClean = entry.tags.map(t => cleanString(t));
      
      searchMatch = titleClean.includes(q) || 
                    descClean.includes(q) || 
                    catClean.includes(q) || 
                    tagsClean.some(tag => tag.includes(q));
    }
    
    return categoryMatch && searchMatch;
  });
  
  if (filtered.length === 0) {
    cardsGrid.innerHTML = `
      <div class="no-results">
        <p>No entries match your exploration parameters.</p>
      </div>
    `;
    return;
  }
  
  cardsGrid.innerHTML = filtered.map((entry) => {
    const statusClass = cleanString(entry.status).replace(/\s+/g, '-').replace(/[^a-z0-9-]/g, '');
    return `
      <article class="theory-card" data-index="${entries.indexOf(entry)}" tabindex="0">
        <div class="card-header">
          <span class="card-category">${entry.category}</span>
          <span class="card-status status-${statusClass}">${entry.status}</span>
        </div>
        <h3 class="card-title">${entry.title}</h3>
        <p class="card-description">${entry.description}</p>
        <div class="card-tags">
          ${entry.tags.map(tag => `<span class="tag">#${tag}</span>`).join('')}
        </div>
      </article>
    `;
  }).join('');
}

// Event Listeners Setup
function setupEventListeners() {
  // Category clicks
  categoryFiltersContainer.addEventListener("click", (e) => {
    const button = e.target.closest(".filter-btn");
    if (!button) return;
    
    activeCategory = button.dataset.category;
    
    // Update active visual class
    document.querySelectorAll(".filter-btn").forEach(btn => {
      btn.classList.toggle("active", btn.dataset.category === activeCategory);
    });
    
    renderCards();
  });
  
  // Search input change
  searchInput.addEventListener("input", (e) => {
    searchQuery = e.target.value;
    renderCards();
  });
  
  // Card clicks to open modal
  cardsGrid.addEventListener("click", (e) => {
    const card = e.target.closest(".theory-card");
    if (!card) return;
    openModal(parseInt(card.dataset.index));
  });
  
  // Support Enter/Space key on cards for accessibility
  cardsGrid.addEventListener("keydown", (e) => {
    if (e.key === "Enter" || e.key === " ") {
      const card = e.target.closest(".theory-card");
      if (card) {
        e.preventDefault();
        openModal(parseInt(card.dataset.index));
      }
    }
  });
  
  // Close buttons and overlay
  modalOverlay.addEventListener("click", closeModal);
  document.getElementById("modal-close-btn").addEventListener("click", closeModal);
  
  // Escape key listener for closing modal
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") {
      closeModal();
    }
  });
}

// Modal handling
function openModal(index) {
  const entry = entries[index];
  if (!entry) return;
  
  const statusClass = cleanString(entry.status).replace(/\s+/g, '-').replace(/[^a-z0-9-]/g, '');
  
  const modalContent = document.getElementById("modal-content-area");
  modalContent.innerHTML = `
    <div class="modal-header">
      <div class="modal-meta">
        <span class="modal-category">${entry.category}</span>
        <span class="modal-status status-${statusClass}">${entry.status}</span>
      </div>
      <h2 class="modal-title">${entry.title}</h2>
    </div>
    
    <div class="modal-body">
      <section class="modal-section intro-section">
        <h3>Description</h3>
        <p class="modal-desc-text">${entry.description}</p>
      </section>
      
      <section class="modal-section">
        <h3>Main Explanation</h3>
        <p>${entry.explanation}</p>
      </section>
      
      <section class="modal-section">
        <h3>Why It's Interesting</h3>
        <p>${entry.whyInteresting}</p>
      </section>
      
      <div class="modal-split">
        <section class="modal-section split-section">
          <h3>Related Ideas</h3>
          <ul class="related-list">
            ${entry.related.map(rel => {
              const relEntry = entries.find(e => e.title === rel);
              if (relEntry) {
                const idx = entries.indexOf(relEntry);
                return `<li><a href="#" class="related-link" data-index="${idx}">${rel}</a></li>`;
              }
              return `<li>${rel}</li>`;
            }).join('')}
          </ul>
        </section>
        
        <section class="modal-section split-section ideas-box">
          <h3>Content Angles & Video Ideas</h3>
          <ul class="ideas-list">
            ${entry.contentIdeas.map(idea => `<li>"${idea}"</li>`).join('')}
          </ul>
        </section>
      </div>
    </div>
    
    <div class="modal-footer">
      <div class="modal-tags">
        ${entry.tags.map(tag => `<span class="tag">#${tag}</span>`).join('')}
      </div>
    </div>
  `;
  
  // Set up click events on the related links inside the modal
  modalContent.querySelectorAll(".related-link").forEach(link => {
    link.addEventListener("click", (e) => {
      e.preventDefault();
      const nextIndex = parseInt(link.dataset.index);
      openModal(nextIndex);
    });
  });
  
  detailModal.classList.add("visible");
  modalOverlay.classList.add("visible");
  document.body.style.overflow = "hidden"; // Prevent background scroll
}

function closeModal() {
  detailModal.classList.remove("visible");
  modalOverlay.classList.remove("visible");
  document.body.style.overflow = "";
}

// Start everything up
document.addEventListener("DOMContentLoaded", init);
