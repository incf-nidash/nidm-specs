% Convenience function to write out cluster and peak entities in FSL ground
% truth
function peak_clusters(featDir)
    clusterTable = readtable(fullfile(featDir, 'cluster_zstat1.txt'), 'Delimiter', '\t', 'ReadrowNames', true);  
    clusterTableStd = readtable(fullfile(featDir, 'cluster_zstat1_std.txt'), 'Delimiter', '\t', 'ReadrowNames', true);  
    
    peakTable = readtable(fullfile(featDir, 'lmax_zstat1.txt'), 'Delimiter', '\t', 'ReadrowNames', true);  
    peakTableStd = readtable(fullfile(featDir, 'lmax_zstat1_std.txt'), 'Delimiter', '\t', 'ReadrowNames', true);  
    
    % Add cluster id for each peak    
    strClusterIds = strvcat(peakTable.Properties.RowNames);
    peakTable.CLUSTER = str2num(strClusterIds(:,1));
    strClusterStdIds = strvcat(peakTableStd.Properties.RowNames);
    peakTableStd.CLUSTER = str2num(strClusterStdIds(:,1));
    
    entities = '';
    
    myfile = fopen('entities.txt', 'w+');
    
    % For each cluster   
    for i = 1:height(clusterTable)
        index = num2str(clusterTable.Properties.RowNames{i});
        entities = [entities ['\n\n' 'entity(niiri:cluster_000' index ',']];
        entities = [entities ['\n\t' '[prov:type = ''nidm:ClusterStatistic'',']];
        entities = [entities ['\n\t' 'prov:label = "Cluster Statistic: 000' index '" %%%% xsd:string,']];
        entities = [entities ['\n\t' 'nidm:clusterSizeInVoxels = "' num2str(clusterTable.Voxels(i)) '" %%%% xsd:int,']];
        entities = [entities ['\n\t' 'nidm:pValueFWER = "' num2str(clusterTable.P(i)) '" %%%% xsd:float])']];
%         entities = [entities ['\n\t' 'nidm:centerOfGarvity = ''niiri:center_of_gravity_' index '''])']];

        entities = [entities ['\n\t' 'wasDerivedFrom(niiri:cluster_000' index ', niiri:excursion_set_id_1)  ']];

        entities = [entities ['\n\n' 'entity(niiri:center_of_gravity_' index ',']];
        entities = [entities ['\n\t' '[prov:type = ''fsl:CenterOfGravity'',']];
        entities = [entities ['\n\t' 'prov:label = "Center of gravity ' index '",']];
        entities = [entities ['\n\t' 'prov:location = ''niiri:COG_coordinate_000' index '''])']];
        
        entities = [entities ['\n\n' 'wasDerivedFrom(niiri:center_of_gravity_' index ', niiri:cluster_000' index ')']];

        entities = [entities ['\n\n' 'entity(niiri:COG_coordinate_000' index ',']];
        entities = [entities ['\n\t' '[prov:type = ''prov:Location'',']];
        entities = [entities ['\n\t' 'prov:type = ''nidm:Coordinate'',']];
        entities = [entities ['\n\t' 'prov:label = "Coordinate 000' index '" %%%% xsd:string,']];
        entities = [entities ['\n\t' 'nidm:coordinate1 = "' num2str(clusterTable.Z_COGX_vox_(i)) '" %%%% xsd:float,']];
        entities = [entities ['\n\t' 'nidm:coordinate2 = "' num2str(clusterTable.Z_COGY_vox_(i)) '" %%%% xsd:float,']];
        entities = [entities ['\n\t' 'nidm:coordinate3 = "' num2str(clusterTable.Z_COGZ_vox_(i)) '" %%%% xsd:float,']];
        entities = [entities ['\n\t' 'nidm:coordinate1InUnits = "' num2str(clusterTableStd{num2str(index),{'Z_COGX_mm_'}}) '" %%%% xsd:float,']];
        entities = [entities ['\n\t' 'nidm:coordinate2InUnits = "' num2str(clusterTableStd{num2str(index),{'Z_COGY_mm_'}}) '" %%%% xsd:float,']];
        entities = [entities ['\n\t' 'nidm:coordinate3InUnits = "' num2str(clusterTableStd{num2str(index),{'Z_COGZ_mm_'}}) '" %%%% xsd:float])  ']];
        
        % For each peak in that cluster
        peaks = peakTable(peakTable.CLUSTER==str2num(clusterTable.Properties.RowNames{i}),:);
        peaksStd = peakTableStd(peakTableStd.CLUSTER==str2num(clusterTable.Properties.RowNames{i}),:);
        for j = 1:height(peaks)
            rowName = peaks.Properties.RowNames{j};
            peakIndex = [index '_' num2str(j)];
            
            entities = [entities ['\n\n' 'entity(niiri:peak_000' peakIndex ',']];
            if j == 1
                entities = [entities ['\n\t' '[prov:type = ''fsl:ClusterMaximumStatistic'',']];
            end
            entities = [entities ['\n\t' 'prov:type = ''nidm:PeakStatistic'',']];
            entities = [entities ['\n\t' 'prov:label = "Peak 000' peakIndex '" %%%% xsd:string,']];
            entities = [entities ['\n\t' 'prov:location = ''niiri:coordinate_000' peakIndex ''',']];
            entities = [entities ['\n\t' 'nidm:equivalentZStatistic = "' num2str(peaks{j,'Z'}) '" %%%% xsd:float])']];

            entities = [entities ['\n\n' 'entity(niiri:coordinate_000' peakIndex ',']];
            entities = [entities ['\n\t' '[prov:type = ''prov:Location'',']];
            entities = [entities ['\n\t' 'prov:type = ''nidm:Coordinate'',']];
            entities = [entities ['\n\t' 'prov:label = "Coordinate 000' peakIndex '" %%%% xsd:string,']];
            entities = [entities ['\n\t' 'nidm:coordinate1 = "' num2str(peaks{j,'x'}) '" %%%% xsd:int,']];
            entities = [entities ['\n\t' 'nidm:coordinate2 = "' num2str(peaks{j,'y'}) '" %%%% xsd:int,']];
            entities = [entities ['\n\t' 'nidm:coordinate3 = "' num2str(peaks{j,'z'}) '" %%%% xsd:int,']];
            entities = [entities ['\n\t' 'nidm:coordinate1InUnits = "' num2str(peaksStd{peaks(j,:).Properties.RowNames, 'x'}) '" %%%% xsd:float,']];
            entities = [entities ['\n\t' 'nidm:coordinate2InUnits = "' num2str(peaksStd{peaks(j,:).Properties.RowNames, 'y'}) '" %%%% xsd:float,']];
            entities = [entities ['\n\t' 'nidm:coordinate3InUnits = "' num2str(peaksStd{peaks(j,:).Properties.RowNames, 'z'}) '" %%%% xsd:float])   ']];     

            entities = [entities ['\n\t' 'wasDerivedFrom(niiri:peak_000' peakIndex ', niiri:cluster_000' index ')']];
        end
    end
    
    fprintf(myfile, entities);
    fclose(myfile)
end