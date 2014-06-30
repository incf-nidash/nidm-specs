% Convenience function to write out coordinate space entities in FSL ground
% truth
function coordinate_spaces(featDir)
    coordinate_space_entity(fullfile(featDir, 'stats', 'sigmasquareds.nii.gz'), 1, true);
    coordinate_space_entity(fullfile(featDir, 'mask.nii.gz'), 2, true);
    coordinate_space_entity(fullfile(featDir, 'stats', 'pe1.nii.gz'), 3, true);
    coordinate_space_entity(fullfile(featDir, 'stats', 'pe2.nii.gz'), 4, true);
    coordinate_space_entity(fullfile(featDir, 'stats', 'pe3.nii.gz'), 5, true);
    coordinate_space_entity(fullfile(featDir, 'stats', 'pe4.nii.gz'), 6, true);
    
    coordinate_space_entity(fullfile(featDir, 'stats', 'cope1.nii.gz'), 7, true);
    coordinate_space_entity(fullfile(featDir, 'stats', 'varcope1.nii.gz'), 8, true);
    coordinate_space_entity(fullfile(featDir, 'stats', 'sqrt_varcope1.nii.gz'), 9, true);
    coordinate_space_entity(fullfile(featDir, 'stats', 'zstat1.nii.gz'), 10, true);
    coordinate_space_entity(fullfile(featDir, 'stats', 'tstat1.nii.gz'), 11, true);
    coordinate_space_entity(fullfile(featDir, 'thresh_zstat1.nii.gz'), 12, true);
end