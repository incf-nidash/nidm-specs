% Convenience function to write out a coordinateSpace entity
function coordinate_space_entity(niftiFile, num, forcedelete)
    [path, name, ext] = spm_fileparts(niftiFile);
    
    gunz = false;
    if strcmp(ext, '.gz')
        gunzip(niftiFile)
        gunz = true;
        niftiFile = fullfile(path, name);
    end

    myfile = fopen('coordinatespace.txt', 'a+');
    
    vol = spm_vol(niftiFile);
    niftiImg = nifti(niftiFile);
    niftiHdr = niftiImg.hdr;
    
    dimensions = [ '[' num2str(vol.dim, '%g, ')];
    dimensions(end) = ']';
    
    voxelSize = [ '[' num2str(niftiHdr.pixdim(2:4), '%g, ')];
    voxelSize(end) = ']';
    
    voxelToWorldMatrix = spm_get_space(niftiFile);
    % SPM to Nifti convention    
    voxelToWorldMatrix(1:3,end) = sign(voxelToWorldMatrix(1:3,end)).*(abs(voxelToWorldMatrix(1:3,end))-niftiHdr.pixdim(2:4)');
    
    voxelToWorldAttribute = '[';
    for i = 1:size(voxelToWorldMatrix, 1)
        voxelToWorldAttribute = [voxelToWorldAttribute '[ '];
        for j = 1:size(voxelToWorldMatrix, 2)
            voxelToWorldAttribute = [voxelToWorldAttribute ...
                num2str(voxelToWorldMatrix(i,j), '%g,')];
            voxelToWorldAttribute = [voxelToWorldAttribute ' '];
        end
        voxelToWorldAttribute(end-1:end+1) = '], ';
%         voxelToWorldAttribute = [voxelToWorldAttribute '], '];
    end
    voxelToWorldAttribute(end) = '';
    voxelToWorldAttribute(end) = ']';
    
    entities = '';
    entities = [entities '\n\n' 'entity(niiri:coordinate_space_id_' num2str(num) ','];
    entities = [entities '\n\t' '[prov:type = ''nidm:CoordinateSpace'','];
    entities = [entities '\n\t' 'prov:label = "Coordinate space ' num2str(num) '" %%%% xsd:string,'];
    entities = [entities '\n\t' 'nidm:voxelToWorldMapping = "' voxelToWorldAttribute '" %%%% xsd:string,'];
    % FIXME: Find units automatically     
    entities = [entities '\n\t' 'nidm:voxelUnits = "[''mm'', ''mm'', ''mm'']" %%%% xsd:string,'];
    entities = [entities '\n\t' 'nidm:voxelSize = "' voxelSize '" %%%% xsd:string,'];
    entities = [entities '\n\t' 'nidm:coordinateSystem = ''nidm:mniCoordinateSystem'','];
    entities = [entities '\n\t' 'nidm:numberOfDimensions = "' num2str(numel(vol.dim)) '" %%%% xsd:int,'];
    entities = [entities '\n\t' 'nidm:dimensions = "' dimensions '" %%%% xsd:string])'];

    fprintf(myfile, entities);
    fclose(myfile);
    
    if gunz
        if ~exist('forcedelete', 'var') || ~forcedelete 
            ButtonName = questdlg('Delete gunzipped?', ...
                             ['Delete gunzipped: ' niftiFile], ...
                             'Yes', 'No', 'No');
        else
            ButtonName = 'Yes';
        end
        switch ButtonName,
         case 'Yes',
          delete(niftiFile);
         case 'No',
          disp('Did not delete gunzipped.')
        end % switch
    end
end