class DisposalGuidance:
    def __init__(self):
        self.guidance_map = {
            "Organic Waste": (
                "• Organic waste such as cooked or raw food scraps can be composted at home using compost bins.\n"
                "• For smelly or wet food like rice, curries, or peels, consider vermicomposting with red wigglers.\n"
                "• Avoid mixing organic waste with plastic packaging or foil wrappers.\n"
                "• Do not dispose in dry or general waste bins as it can contaminate recyclables.\n"
                "• Many municipalities provide green or brown bins specifically for food and garden waste.\n"
                "• Ensure no inorganic items like plastic containers or sachets are mixed in."
            ),
            "Plastic": (
                "• Rinse plastic containers to remove any food residue before recycling.\n"
                "• Sort plastic by type (e.g., PET, HDPE) if required by your region.\n"
                "• Soft plastics (like wrappers) may not be recyclable curbside.\n"
                "• Never burn plastic waste — it releases toxic chemicals.\n"
                "• Avoid mixing contaminated plastic with clean recyclables.\n"
                "• Consider reusable alternatives to single-use plastics."
            ),
            "Contaminated Plastic": (
                "• Plastic items with food residue (e.g., curry containers) must be washed thoroughly.\n"
                "• If cleaning is not possible, dispose in dry waste — do not recycle.\n"
                "• Contaminated plastic can ruin entire recycling batches.\n"
                "• For greasy plastic wraps or oily coatings, treat as landfill waste.\n"
                "• Encourage proper separation of food and plastic at source.\n"
                "• Use compostable packaging for food where possible."
            ),
            "Paper": (
                "• Clean, dry paper can be recycled — sort into blue bin or paper-specific container.\n"
                "• Shredded paper may not be accepted everywhere — check with your local center.\n"
                "• Avoid folding oily or food-stained paper into recycling.\n"
                "• Consider reusing paper for notes or packing before discarding.\n"
                "• Flatten cardboard to save space in bins.\n"
                "• Wet or contaminated paper must go to landfill or compost depending on condition."
            ),
            "Contaminated Paper": (
                "• Paper with grease, food stains, or liquid damage is not recyclable.\n"
                "• Pizza boxes with grease should be composted if allowed — or discarded as landfill.\n"
                "• Do not mix contaminated paper with clean paper in recycling.\n"
                "• Remove clean parts (e.g., lid of box) and recycle separately if possible.\n"
                "• Wet tissue, napkins, and oily paper are treated as biodegradable waste.\n"
                "• Use clean alternatives next time (e.g., wax wrap, reusable plates)."
            ),
            "Glass": (
                "• Rinse glass bottles and jars before recycling.\n"
                "• Wrap broken glass in newspaper before discarding to prevent injury.\n"
                "• Do not mix ceramics or mirrors with regular glass recycling.\n"
                "• Colored and clear glass may need separate sorting.\n"
                "• Reuse glass jars for storage when possible.\n"
                "• Avoid placing heat-treated glass like Pyrex in recycling bins."
            ),
            "Metal": (
                "• Rinse metal cans to remove any food or drink residue.\n"
                "• Crushed cans can save space in your bin but ensure they’re clean.\n"
                "• Separate metal lids from glass jars before recycling.\n"
                "• Aluminum foil can be recycled if clean and balled.\n"
                "• Avoid sharp edges that may injure sorting workers.\n"
                "• Use refillable containers to reduce metal waste."
            ),
            "Composite": (
                "• Composite items (like foil-lined chip packets or Tetra Paks) are made of multiple layers.\n"
                "• Most cannot be separated at regular recycling facilities.\n"
                "• Dispose in landfill or check for special collection programs.\n"
                "• Do not mix with plastics or paper in regular bins.\n"
                "• Some brands now offer drop-off recycling for multilayer packaging.\n"
                "• Use single-material packaging whenever possible."
            ),
            "E-Waste": (
                "• Items like chargers, batteries, and cables must go to certified e-waste collection centers.\n"
                "• Do not throw electronics in household bins — they contain hazardous metals.\n"
                "• Many cities offer free e-waste pickup or drop-off points.\n"
                "• Reuse or donate working devices to reduce e-waste.\n"
                "• Remove batteries before disposing of electronics.\n"
                "• Label damaged electronics clearly before discarding."
            ),
            "Hazardous Waste": (
                "• Do not throw medicines, chemicals, or paints into regular bins.\n"
                "• Hazardous waste must be handled by approved facilities.\n"
                "• Store items like pesticides, solvents, and cleaners in sealed containers.\n"
                "• Participate in your city’s hazardous waste collection days.\n"
                "• Keep hazardous waste away from children and pets.\n"
                "• Never pour chemicals down the drain or toilet."
            ),
            "Textile": (
                "• Donate clean, wearable clothes to local shelters or NGOs.\n"
                "• For damaged or torn fabrics, check for textile recycling programs.\n"
                "• Avoid sending large amounts of textiles to landfill — they take decades to degrade.\n"
                "• Separate synthetic and natural fabrics when possible.\n"
                "• Reuse clothes as rags or upcycle creatively before discarding.\n"
                "• Dry textiles fully before disposal to prevent mold."
            ),
            "Unknown": (
                "• The item could not be confidently classified.\n"
                "• Please rephrase or describe the item in more detail (e.g., its material or usage).\n"
                "• Avoid abstract words like 'beautiful', 'education', or 'happiness'.\n"
                "• Try adding object-related keywords like 'wrapper', 'box', or 'container'.\n"
                "• You can enter multiple descriptive words for better results.\n"
                "• This helps the system guide you with accurate disposal suggestions."
            )
        }

    def get_guidance(self, material_type: str) -> str:
        return self.guidance_map.get(material_type, self.guidance_map["Unknown"])
