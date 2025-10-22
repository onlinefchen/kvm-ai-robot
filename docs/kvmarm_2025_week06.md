# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2025-10-22 07:57:59

**分析周期**: 最近 7 天

## 📊 总体统计

- **总邮件数**: 217
- **总 Thread 数**: 27
- **大型 Thread** (>20封): 3 个

### 分类分布

- **PATCH**: 21 threads (196 邮件)
- **RFC**: 3 threads (15 邮件)
- **Question**: 1 threads (1 邮件)
- **GIT PULL**: 1 threads (2 邮件)
- **Other**: 1 threads (3 邮件)

---

## 📌 PATCH

共 21 个 thread

---

### Thread 1: [PATCH v19 00/11] arm64/perf: Enable branch stack sampling

**📧 邮件数**: 31 | **👥 参与者**: 4 | **📅 开始时间**: Sun, 02 Feb 2025 18:42:54 -0600

#### 🤖 AI 总结

本邮件线程讨论了针对 ARM64 架构的分支记录缓冲扩展（BRBE）的补丁系列，主要集中在性能监控（perf）方面的支持。

1. **原始补丁内容**：补丁系列的目的是在 ARM64 上启用 BRBE 支持，BRBE 是 ARMv9.2 架构的一项特性，旨在记录执行过程中分支的信息。补丁包括对现有代码的清理和对 BRBE 支持的具体实现。

2. **之前讨论要点**：在历史讨论中，参与者们对补丁的设计和实现进行了深入探讨，特别是如何处理分支记录的过滤和事件的排除设置。补丁的设计考虑了与现有 x86 架构的兼容性，并确保在虚拟化环境中正确处理 BRBE。

3. **本周的新讨论与进展**：本周的讨论中，参与者对补丁的各个部分进行了审查和反馈，确认了多个补丁的有效性（如对事件过滤的处理和 BRBE 的初始化）。同时，针对如何在虚拟机环境中处理 BRBE 记录的建议也引发了讨论，部分参与者认为应允许在客人环境中使用 BRBE。最终，补丁系列得到了多个参与者的认可，预计将进一步推动 BRBE 的实现和优化。

整体来看，此次讨论不仅关注技术细节，还涉及到如何在不同环境下有效利用 BRBE 的潜力，确保其在性能监控中的有效性和灵活性。

#### 📝 邮件列表

1. **[02-02 18:42]** [PATCH v19 00/11] arm64/perf: Enable branch stack sampling
   - 发件人: Rob Herring (Arm) <robh@kernel.org>
2. **[02-02 18:42]** [PATCH v19 01/11] perf: arm_pmuv3: Call kvm_vcpu_pmu_resync_el0()
 before enabling counters
   - 发件人: Rob Herring (Arm) <robh@kernel.org>
3. **[02-02 18:42]** [PATCH v19 02/11] perf: arm_pmu: Don't disable counter in
 armpmu_add()
   - 发件人: Rob Herring (Arm) <robh@kernel.org>
4. **[02-02 18:42]** [PATCH v19 03/11] perf: arm_pmuv3: Don't disable counter in
 armv8pmu_enable_event()
   - 发件人: Rob Herring (Arm) <robh@kernel.org>
5. **[02-02 18:42]** [PATCH v19 04/11] perf: arm_v7_pmu: Drop obvious comments for
 enabling/disabling counters and interrupts
   - 发件人: Rob Herring (Arm) <robh@kernel.org>
6. **[02-02 18:42]** [PATCH v19 05/11] perf: arm_v7_pmu: Don't disable counter in
 (armv7|krait_|scorpion_)pmu_enable_event()
   - 发件人: Rob Herring (Arm) <robh@kernel.org>
7. **[02-02 18:43]** [PATCH v19 06/11] perf: apple_m1: Don't disable counter in
 m1_pmu_enable_event()
   - 发件人: Rob Herring (Arm) <robh@kernel.org>
8. **[02-02 18:43]** [PATCH v19 07/11] perf: arm_pmu: Move PMUv3-specific data
   - 发件人: Rob Herring (Arm) <robh@kernel.org>
9. **[02-02 18:43]** [PATCH v19 08/11] arm64/sysreg: Add BRBE registers and fields
   - 发件人: Rob Herring (Arm) <robh@kernel.org>
10. **[02-02 18:43]** [PATCH v19 09/11] arm64: Handle BRBE booting requirements
   - 发件人: Rob Herring (Arm) <robh@kernel.org>
11. **[02-02 18:43]** [PATCH v19 10/11] KVM: arm64: nvhe: Disable branch generation in
 nVHE guests
   - 发件人: Rob Herring (Arm) <robh@kernel.org>
12. **[02-02 18:43]** [PATCH v19 11/11] perf: arm_pmuv3: Add support for the Branch
 Record Buffer Extension (BRBE)
   - 发件人: Rob Herring (Arm) <robh@kernel.org>
13. **[02-03 09:37]** Re: [PATCH v19 01/11] perf: arm_pmuv3: Call kvm_vcpu_pmu_resync_el0()
 before enabling counters
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
14. **[02-03 09:39]** Re: [PATCH v19 04/11] perf: arm_v7_pmu: Drop obvious comments for
 enabling/disabling counters and interrupts
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
15. **[02-03 11:34]** Re: [PATCH v19 02/11] perf: arm_pmu: Don't disable counter in
 armpmu_add()
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
16. **[02-03 12:08]** Re: [PATCH v19 03/11] perf: arm_pmuv3: Don't disable counter in
 armv8pmu_enable_event()
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
17. **[02-03 12:24]** Re: [PATCH v19 05/11] perf: arm_v7_pmu: Don't disable counter in
 (armv7|krait_|scorpion_)pmu_enable_event()
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
18. **[02-03 13:40]** Re: [PATCH v19 06/11] perf: apple_m1: Don't disable counter in
 m1_pmu_enable_event()
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
19. **[02-03 13:46]** Re: [PATCH v19 07/11] perf: arm_pmu: Move PMUv3-specific data
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
20. **[02-03 14:02]** Re: [PATCH v19 08/11] arm64/sysreg: Add BRBE registers and fields
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
21. **[02-03 14:17]** Re: [PATCH v19 09/11] arm64: Handle BRBE booting requirements
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
22. **[02-03 14:46]** Re: [PATCH v19 10/11] KVM: arm64: nvhe: Disable branch generation in
 nVHE guests
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
23. **[02-03 11:28]** Re: [PATCH v19 10/11] KVM: arm64: nvhe: Disable branch generation in
 nVHE guests
   - 发件人: James Clark <james.clark@linaro.org>
24. **[02-03 16:53]** Re: [PATCH v19 11/11] perf: arm_pmuv3: Add support for the Branch
 Record Buffer Extension (BRBE)
   - 发件人: James Clark <james.clark@linaro.org>
25. **[02-03 11:58]** Re: [PATCH v19 11/11] perf: arm_pmuv3: Add support for the Branch
 Record Buffer Extension (BRBE)
   - 发件人: Rob Herring <robh@kernel.org>
26. **[02-04 12:02]** Re: [PATCH v19 11/11] perf: arm_pmuv3: Add support for the Branch
 Record Buffer Extension (BRBE)
   - 发件人: James Clark <james.clark@linaro.org>
27. **[02-04 09:03]** Re: [PATCH v19 11/11] perf: arm_pmuv3: Add support for the Branch
 Record Buffer Extension (BRBE)
   - 发件人: Rob Herring <robh@kernel.org>
28. **[02-05 14:38]** Re: [PATCH v19 11/11] perf: arm_pmuv3: Add support for the Branch
 Record Buffer Extension (BRBE)
   - 发件人: James Clark <james.clark@linaro.org>
29. **[02-05 14:51]** Re: [PATCH v19 11/11] perf: arm_pmuv3: Add support for the Branch
 Record Buffer Extension (BRBE)
   - 发件人: James Clark <james.clark@linaro.org>
30. **[02-05 10:15]** Re: [PATCH v19 11/11] perf: arm_pmuv3: Add support for the Branch
 Record Buffer Extension (BRBE)
   - 发件人: Rob Herring <robh@kernel.org>
31. **[02-06 12:58]** Re: [PATCH v19 11/11] perf: arm_pmuv3: Add support for the Branch
 Record Buffer Extension (BRBE)
   - 发件人: James Clark <james.clark@linaro.org>

---

### Thread 2: [PATCH v6 12/43] arm64: RME: Allocate/free RECs to match vCPUs

**📧 邮件数**: 23 | **👥 参与者**: 4 | **📅 开始时间**: Wed, 29 Jan 2025 14:50:21 +1000

#### 🤖 AI 总结

本邮件讨论主题为“[PATCH v6 12/43] arm64: RME: Allocate/free RECs to match vCPUs”，主要围绕在 ARM64 架构下为虚拟 CPU (vCPU) 分配和释放 RECs（Realm Control Structures）进行讨论。

**原始 patch/问题的内容**：
该补丁旨在确保为每个 vCPU 分配和释放相应的 RECs，以优化资源管理和性能。

**之前讨论要点**：
在历史讨论中，参与者对补丁的实现细节进行了多次评审和建议。例如，Steven Price 提出了一些函数命名的改进建议，并指出某些检查是多余的。此外，Gavin Shan 也提到了一些边界情况的处理，确保在没有 RME 支持的系统上不会增加额外开销。

**本周的新讨论、进展或结论**：
本周的讨论中，Suzuki K Poulose 和 Steven Price 继续对补丁进行细化，讨论了如何更有效地传递 kvm 指针以优化功能检查。Steven 还确认了对函数命名的修改，并讨论了如何处理内存故障的逻辑，以减少资源管理中的冲突。此外，参与者们一致同意对一些函数的命名进行更改，以提高代码的可读性和一致性。整体来看，本周的讨论集中在细节优化和代码清晰度上，推动了补丁的进一步完善。

#### 📝 邮件列表

1. **[01-29 14:50]** Re: [PATCH v6 12/43] arm64: RME: Allocate/free RECs to match vCPUs
   - 发件人: Gavin Shan <gshan@redhat.com>
2. **[01-30 09:41]** Re: [PATCH v6 17/43] arm64: RME: Handle realm enter/exit
   - 发件人: Gavin Shan <gshan@redhat.com>
3. **[01-30 14:38]** Re: [PATCH v6 19/43] arm64: RME: Allow populating initial contents
   - 发件人: Gavin Shan <gshan@redhat.com>
4. **[01-30 15:22]** Re: [PATCH v6 20/43] arm64: RME: Runtime faulting of memory
   - 发件人: Gavin Shan <gshan@redhat.com>
5. **[01-30 16:40]** Re: [PATCH v6 12/43] arm64: RME: Allocate/free RECs to match vCPUs
   - 发件人: Steven Price <steven.price@arm.com>
6. **[02-02 11:22]** Re: [PATCH v6 22/43] KVM: arm64: Validate register access for a Realm
 VM
   - 发件人: Gavin Shan <gshan@redhat.com>
7. **[02-02 12:15]** Re: [PATCH v6 25/43] arm64: Don't expose stolen time for realm guests
   - 发件人: Gavin Shan <gshan@redhat.com>
8. **[02-02 16:00]** Re: [PATCH v6 28/43] arm64: rme: Allow checking SVE on VM instance
   - 发件人: Gavin Shan <gshan@redhat.com>
9. **[02-02 16:41]** Re: [PATCH v6 27/43] arm64: rme: support RSI_HOST_CALL
   - 发件人: Gavin Shan <gshan@redhat.com>
10. **[02-02 16:52]** Re: [PATCH v6 29/43] arm64: RME: Always use 4k pages for realms
   - 发件人: Gavin Shan <gshan@redhat.com>
11. **[02-02 17:12]** Re: [PATCH v6 30/43] arm64: rme: Prevent Device mappings for Realms
   - 发件人: Gavin Shan <gshan@redhat.com>
12. **[02-03 11:18]** Re: [PATCH v6 12/43] arm64: RME: Allocate/free RECs to match vCPUs
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
13. **[02-03 16:34]** Re: [PATCH v6 17/43] arm64: RME: Handle realm enter/exit
   - 发件人: Steven Price <steven.price@arm.com>
14. **[02-03 16:34]** Re: [PATCH v6 12/43] arm64: RME: Allocate/free RECs to match vCPUs
   - 发件人: Steven Price <steven.price@arm.com>
15. **[02-03 16:52]** Re: [PATCH v6 19/43] arm64: RME: Allow populating initial contents
   - 发件人: Steven Price <steven.price@arm.com>
16. **[02-06 10:03]** Re: [PATCH v6 20/43] arm64: RME: Runtime faulting of memory
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
17. **[02-07 17:04]** Re: [PATCH v6 20/43] arm64: RME: Runtime faulting of memory
   - 发件人: Steven Price <steven.price@arm.com>
18. **[02-07 17:04]** Re: [PATCH v6 22/43] KVM: arm64: Validate register access for a Realm
 VM
   - 发件人: Steven Price <steven.price@arm.com>
19. **[02-07 17:05]** Re: [PATCH v6 25/43] arm64: Don't expose stolen time for realm guests
   - 发件人: Steven Price <steven.price@arm.com>
20. **[02-07 17:05]** Re: [PATCH v6 27/43] arm64: rme: support RSI_HOST_CALL
   - 发件人: Steven Price <steven.price@arm.com>
21. **[02-07 17:05]** Re: [PATCH v6 28/43] arm64: rme: Allow checking SVE on VM instance
   - 发件人: Steven Price <steven.price@arm.com>
22. **[02-07 17:05]** Re: [PATCH v6 29/43] arm64: RME: Always use 4k pages for realms
   - 发件人: Steven Price <steven.price@arm.com>
23. **[02-07 17:08]** Re: [PATCH v6 30/43] arm64: rme: Prevent Device mappings for Realms
   - 发件人: Steven Price <steven.price@arm.com>

---

### Thread 3: [PATCH 00/15] arm: rework id register storage

**📧 邮件数**: 22 | **👥 参与者**: 3 | **📅 开始时间**: Fri,  7 Feb 2025 12:02:33 +0100

#### 🤖 AI 总结

本邮件线程讨论了对 ARM 架构中 ID 寄存器存储的重构，主要集中在一系列补丁（共15个）上，旨在改进 CPU 模型的支持。

1. **原始补丁/问题内容**：
   该补丁系列的核心是重新设计 ARM 架构的 ID 寄存器存储方式，目的是为 CPU 模型的支持奠定基础。补丁中包括了对 ID 寄存器的存储方式的更改，采用枚举类型进行索引，并更新了生成寄存器描述的脚本。

2. **之前讨论要点**：
   在之前的讨论中，参与者们探讨了如何更有效地管理和生成 ID 寄存器的定义，尤其是如何将寄存器的字段信息整合到一个结构化的系统中。补丁的设计考虑了未来的扩展性和维护性。

3. **本周的新讨论与进展**：
   本周的讨论中，Cornelia Huck 提出了新的补丁，增加了生成系统寄存器定义的脚本，并引入了新的初始化函数以处理生成的 ID 寄存器定义。Marc Zyngier 和 Richard Henderson 对补丁提出了一些建议和批评，尤其是关于类型安全和生成文件的管理，强调应避免在头文件中直接包含生成的文件，建议在构建时生成这些文件。

整体来看，邮件线程展示了对 ARM CPU 模型寄存器管理的深入讨论，涉及到代码结构、生成机制和未来的可扩展性。

#### 📝 邮件列表

1. **[02-07 12:02]** [PATCH 00/15] arm: rework id register storage
   - 发件人: Cornelia Huck <cohuck@redhat.com>
2. **[02-07 12:02]** [PATCH 01/15] arm/cpu: Add sysreg definitions in cpu-sysregs.h
   - 发件人: Cornelia Huck <cohuck@redhat.com>
3. **[02-07 12:02]** [PATCH 02/15] arm/kvm: add accessors for storing host features into idregs
   - 发件人: Cornelia Huck <cohuck@redhat.com>
4. **[02-07 12:02]** [PATCH 03/15] arm/cpu: Store aa64isar0 into the idregs arrays
   - 发件人: Cornelia Huck <cohuck@redhat.com>
5. **[02-07 12:02]** [PATCH 04/15] arm/cpu: Store aa64isar1/2 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
6. **[02-07 12:02]** [PATCH 05/15] arm/cpu: Store aa64pfr0/1 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
7. **[02-07 12:02]** [PATCH 06/15] arm/cpu: Store aa64mmfr0-3 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
8. **[02-07 12:02]** [PATCH 07/15] arm/cpu: Store aa64dfr0/1 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
9. **[02-07 12:02]** [PATCH 08/15] arm/cpu: Store aa64smfr0 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
10. **[02-07 12:02]** [PATCH 09/15] arm/cpu: Store id_isar0-7 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
11. **[02-07 12:02]** [PATCH 10/15] arm/cpu: Store id_mfr0/1 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
12. **[02-07 12:02]** [PATCH 11/15] arm/cpu: Store id_dfr0/1 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
13. **[02-07 12:02]** [PATCH 12/15] arm/cpu: Store id_mmfr0-5 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
14. **[02-07 12:02]** [PATCH 13/15] arm/cpu: Add infra to handle generated ID register definitions
   - 发件人: Cornelia Huck <cohuck@redhat.com>
15. **[02-07 12:02]** [PATCH 14/15] arm/cpu: Add sysreg generation scripts
   - 发件人: Cornelia Huck <cohuck@redhat.com>
16. **[02-07 12:02]** [PATCH 15/15] arm/cpu: Add generated files
   - 发件人: Cornelia Huck <cohuck@redhat.com>
17. **[02-07 14:14]** Re: [PATCH 14/15] arm/cpu: Add sysreg generation scripts
   - 发件人: Marc Zyngier <maz@kernel.org>
18. **[02-07 10:34]** Re: [PATCH 01/15] arm/cpu: Add sysreg definitions in cpu-sysregs.h
   - 发件人: Richard Henderson <richard.henderson@linaro.org>
19. **[02-07 10:43]** Re: [PATCH 02/15] arm/kvm: add accessors for storing host features
 into idregs
   - 发件人: Richard Henderson <richard.henderson@linaro.org>
20. **[02-07 10:46]** Re: [PATCH 03/15] arm/cpu: Store aa64isar0 into the idregs arrays
   - 发件人: Richard Henderson <richard.henderson@linaro.org>
21. **[02-07 10:50]** Re: [PATCH 02/15] arm/kvm: add accessors for storing host features
 into idregs
   - 发件人: Richard Henderson <richard.henderson@linaro.org>
22. **[02-07 11:02]** Re: [PATCH 15/15] arm/cpu: Add generated files
   - 发件人: Richard Henderson <richard.henderson@linaro.org>

---

### Thread 4: [PATCH 0/3] KVM/arm64: timer fixes for 6.14

**📧 邮件数**: 18 | **👥 参与者**: 4 | **📅 开始时间**: Tue, 28 Jan 2025 16:17:18 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM/arm64 的定时器修复补丁，旨在解决在 6.14 版本中发现的一些问题。历史讨论中，Marc Zyngier 提出了三个补丁，分别针对定时器的软定时器评估、EL1 定时器仿真处理以及虚拟定时器的配置进行了修复。这些问题主要涉及定时器状态的错误处理和性能优化，尤其是在虚拟化环境中。

本周的新讨论中，Dmytro Terletskyi 和 Alexander Potapenko 对之前的补丁进行了测试，并确认其有效性，均表示通过测试。Marc Zyngier 还提出了针对 vgic 的一系列修复补丁，解决了在并发情况下 vgic 被销毁的问题。这些补丁包括删除不必要的警告、检查未分配的 PPI/SPI 数组以及优雅地处理未分配中断的重置。Oliver Upton 对这些补丁表示了认可，并提出了关于如何更好地管理 vgic 的建议，包括可能的引用计数方案。

总体来看，本周的讨论集中在对补丁的测试反馈和对 vgic 问题的进一步探讨上，显示出社区对提高 KVM/arm64 的稳定性和性能的持续关注。

#### 📝 邮件列表

1. **[01-28 16:17]** [PATCH 0/3] KVM/arm64: timer fixes for 6.14
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[01-28 16:17]** [PATCH 1/3] KVM: arm64: timer: Always evaluate the need for a soft timer
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[01-28 16:17]** [PATCH 2/3] KVM: arm64: timer: Correctly handle EL1 timer emulation when !FEAT_ECV
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[01-28 16:17]** [PATCH 3/3] KVM: arm64: timer: Consolidate NV configuration of virtual timers
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[02-04 14:08]** Re: [PATCH 1/3] KVM: arm64: timer: Always evaluate the need for a
 soft timer
   - 发件人: Dmytro Terletskyi <Dmytro_Terletskyi@epam.com>
6. **[02-04 14:10]** Re: [PATCH 2/3] KVM: arm64: timer: Correctly handle EL1 timer
 emulation when !FEAT_ECV
   - 发件人: Dmytro Terletskyi <Dmytro_Terletskyi@epam.com>
7. **[02-04 14:15]** Re: [PATCH 3/3] KVM: arm64: timer: Consolidate NV configuration of
 virtual timers
   - 发件人: Dmytro Terletskyi <Dmytro_Terletskyi@epam.com>
8. **[02-06 15:20]** [PATCH 0/3] KVM: arm64: Assorted vgic fixes for 6.14
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[02-06 15:20]** [PATCH 1/3] KVM: arm64: timer: Drop warning on failed interrupt signalling
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[02-06 15:20]** [PATCH 2/3] KVM: arm64: vgic: Check for unallocated PPI/SPI arrays
   - 发件人: Marc Zyngier <maz@kernel.org>
11. **[02-06 15:21]** [PATCH 3/3] KVM: arm64: vgic: Gracefully handle resetting an unallocated interrupt
   - 发件人: Marc Zyngier <maz@kernel.org>
12. **[02-06 16:50]** Re: [PATCH 1/3] KVM: arm64: timer: Drop warning on failed interrupt signalling
   - 发件人: Alexander Potapenko <glider@google.com>
13. **[02-06 16:50]** Re: [PATCH 2/3] KVM: arm64: vgic: Check for unallocated PPI/SPI arrays
   - 发件人: Alexander Potapenko <glider@google.com>
14. **[02-06 16:50]** Re: [PATCH 3/3] KVM: arm64: vgic: Gracefully handle resetting an
 unallocated interrupt
   - 发件人: Alexander Potapenko <glider@google.com>
15. **[02-07 10:03]** Re: [PATCH 0/3] KVM: arm64: Assorted vgic fixes for 6.14
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
16. **[02-07 18:10]** Re: [PATCH 0/3] KVM: arm64: Assorted vgic fixes for 6.14
   - 发件人: Marc Zyngier <maz@kernel.org>
17. **[02-07 10:50]** Re: [PATCH 0/3] KVM: arm64: Assorted vgic fixes for 6.14
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
18. **[02-08 15:15]** Re: [PATCH 0/3] KVM: arm64: Assorted vgic fixes for 6.14
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 5: [PATCH v3 00/16] KVM: arm64: Add NV GICv3 support

**📧 邮件数**: 17 | **👥 参与者**: 1 | **📅 开始时间**: Thu,  6 Feb 2025 15:49:09 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构上增加对 NV GICv3 支持的补丁（PATCH v3 00/16）。该补丁的主要内容是为 GICv3 提供虚拟化支持，以便在嵌套虚拟化环境中更好地处理中断。

在历史讨论中，Marc Zyngier 提到该补丁是对之前版本的重发，主要修复了默认值和初始化问题，并感谢了 Andre Przywara 的反馈。补丁中包括多个新功能和修复，涉及 GICv3 的多个寄存器和中断处理逻辑。

本周的新讨论中，Marc Zyngier 继续提交了多个补丁，主要包括：
1. **加载顺序调整**：确保在加载 GIC 之前先加载定时器，以便在 L2 客户机中正确处理中断。
2. **维护中断的仿真**：添加了对维护中断（MI）的支持，确保在 L2 运行时能够正确处理 MI。
3. **嵌套 GICv3 的仿真**：实现了 L2 到 L1 的中断注入机制，确保在 L1 中能够正确处理来自 L2 的中断请求。
4. **用户空间接口**：允许用户空间设置 VGIC 维护中断的 IRQ 编号，以便在嵌套虚拟化中使用。

此外，Marc Zyngier 还强调了在没有 GICv3 的情况下初始化 KVM 将失败，确保虚拟化环境的兼容性。

总体而言，本周的讨论集中在增强 GICv3 支持的细节和确保嵌套虚拟化的稳定性上，补丁的逐步完善将有助于提升 KVM 在 arm64 平台上的性能和功能。

#### 📝 邮件列表

1. **[02-06 15:49]** [PATCH v3 00/16] KVM: arm64: Add NV GICv3 support
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[02-06 15:49]** [PATCH v3 01/16] arm64: sysreg: Add layout for ICH_HCR_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[02-06 15:49]** [PATCH v3 02/16] arm64: sysreg: Add layout for ICH_VTR_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[02-06 15:49]** [PATCH v3 03/16] arm64: sysreg: Add layout for ICH_MISR_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[02-06 15:49]** [PATCH v3 04/16] KVM: arm64: nv: Load timer before the GIC
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[02-06 15:49]** [PATCH v3 05/16] KVM: arm64: nv: Add ICH_*_EL2 registers to vpcu_sysreg
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[02-06 15:49]** [PATCH v3 06/16] KVM: arm64: nv: Plumb handling of GICv3 EL2 accesses
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[02-06 15:49]** [PATCH v3 07/16] KVM: arm64: nv: Sanitise ICH_HCR_EL2 accesses
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[02-06 15:49]** [PATCH v3 08/16] KVM: arm64: nv: Nested GICv3 emulation
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[02-06 15:49]** [PATCH v3 09/16] KVM: arm64: nv: Handle L2->L1 transition on interrupt injection
   - 发件人: Marc Zyngier <maz@kernel.org>
11. **[02-06 15:49]** [PATCH v3 10/16] KVM: arm64: nv: Add Maintenance Interrupt emulation
   - 发件人: Marc Zyngier <maz@kernel.org>
12. **[02-06 15:49]** [PATCH v3 11/16] KVM: arm64: nv: Respect virtual HCR_EL2.TWx setting
   - 发件人: Marc Zyngier <maz@kernel.org>
13. **[02-06 15:49]** [PATCH v3 12/16] KVM: arm64: nv: Request vPE doorbell upon nested ERET to L2
   - 发件人: Marc Zyngier <maz@kernel.org>
14. **[02-06 15:49]** [PATCH v3 13/16] KVM: arm64: nv: Propagate used_lrs between L1 and L0 contexts
   - 发件人: Marc Zyngier <maz@kernel.org>
15. **[02-06 15:49]** [PATCH v3 14/16] KVM: arm64: nv: Fold GICv3 host trapping requirements into guest setup
   - 发件人: Marc Zyngier <maz@kernel.org>
16. **[02-06 15:49]** [PATCH v3 15/16] KVM: arm64: nv: Allow userland to set VGIC maintenance IRQ
   - 发件人: Marc Zyngier <maz@kernel.org>
17. **[02-06 15:49]** [PATCH v3 16/16] KVM: arm64: nv: Fail KVM init if asking for NV without GICv3
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 6: [PATCH v2 00/14] KVM: arm64: Support FEAT_PMUv3 on Apple hardware

**📧 邮件数**: 15 | **👥 参与者**: 1 | **📅 开始时间**: Mon,  3 Feb 2025 10:30:57 -0800

#### 🤖 AI 总结

本邮件线程讨论了一个针对 Apple 硬件的 KVM (Kernel-based Virtual Machine) 的补丁系列，主要是为了支持 PMUv3（性能监控单元版本3）在 Apple M 系列处理器上的虚拟化。

1. **原始补丁内容**：补丁系列（共14个补丁）旨在为 Apple 硬件实现 PMUv3 模拟，允许在虚拟机中使用性能监控功能。补丁包括对 PMU 事件的映射、事件过滤、以及在 KVM 中的支持等。

2. **之前讨论要点**：虽然邮件中没有明确提到历史讨论，但补丁的 v2 版本相较于 v1 进行了重构和修复，确保了与 Linux 内核 6.14-rc1 的兼容性，并修复了编译问题。

3. **本周的新讨论和进展**：本周的讨论集中在补丁的具体实现上，包括：
   - 对 Apple M1 和 M2 处理器的 PMUv3 事件映射和过滤的支持。
   - 计算 PMCEID（性能监控事件 ID）以便在虚拟化环境中使用。
   - 引入了新的 CPU 特性检查，以确定系统是否支持 PMUv3。
   - 处理 Apple 硬件的特定陷阱，并提供合成的 ESR（异常状态寄存器）以支持 KVM 的异常处理。
   - 最后，补丁还确保了在支持 IMPDEF 陷阱的硬件上可以正确报告 PMUv3 的存在。

总的来说，这一系列补丁旨在增强 KVM 在 Apple 硬件上的性能监控能力，确保虚拟化环境中的性能计数器能够正常工作。

#### 📝 邮件列表

1. **[02-03 10:30]** [PATCH v2 00/14] KVM: arm64: Support FEAT_PMUv3 on Apple hardware
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[02-03 10:30]** [PATCH v2 01/14] drivers/perf: apple_m1: Refactor event select/filter configuration
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[02-03 10:30]** [PATCH v2 02/14] drivers/perf: apple_m1: Support host/guest event filtering
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
4. **[02-03 10:31]** [PATCH v2 03/14] drivers/perf: apple_m1: Provide helper for mapping PMUv3 events
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
5. **[02-03 10:31]** [PATCH v2 04/14] KVM: arm64: Compute PMCEID from arm_pmu's event bitmaps
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
6. **[02-03 10:31]** [PATCH v2 05/14] KVM: arm64: Always support SW_INCR PMU event
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
7. **[02-03 10:31]** [PATCH v2 06/14] KVM: arm64: Remap PMUv3 events onto hardware
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
8. **[02-03 10:31]** [PATCH v2 07/14] KVM: arm64: Use a cpucap to determine if system supports FEAT_PMUv3
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
9. **[02-03 10:31]** [PATCH v2 08/14] KVM: arm64: Drop kvm_arm_pmu_available static key
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
10. **[02-03 10:31]** [PATCH v2 09/14] KVM: arm64: Use guard() to cleanup usage of arm_pmus_lock
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
11. **[02-03 10:31]** [PATCH v2 10/14] KVM: arm64: Move PMUVer filtering into KVM code
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
12. **[02-03 10:31]** [PATCH v2 11/14] KVM: arm64: Compute synthetic sysreg ESR for Apple PMUv3 traps
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
13. **[02-03 10:31]** [PATCH v2 12/14] KVM: arm64: Advertise PMUv3 if IMPDEF traps are present
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
14. **[02-03 10:31]** [PATCH v2 13/14] KVM: arm64: Provide 1 event counter on IMPDEF hardware
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
15. **[02-03 10:31]** [PATCH v2 14/14] arm64: Enable IMP DEF PMUv3 traps on Apple M*
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 7: [PATCH 1/2] perf: arm_pmuv3: Remove cyclical dependency with kvm_host.h

**📧 邮件数**: 11 | **👥 参与者**: 4 | **📅 开始时间**: Tue,  4 Feb 2025 19:57:07 +0000

#### 🤖 AI 总结

本邮件线程讨论了两个主要的补丁（patch），旨在解决 ARM 架构下 KVM 和 PMU 之间的循环依赖问题。

1. **原始补丁内容**：
   - 第一个补丁（PATCH 1/2）提出移除 `kvm_host.h` 中的循环依赖。当前 `kvm_host.h` 包含了 `arm_pmu.h`，而 `arm_pmu.h` 又反过来包含了 `kvm_host.h`，导致编译问题。补丁建议将 `kvm_host.h` 的部分功能移动到 `arm_pmuv3.h` 中，以打破这一循环。

2. **之前讨论要点**：
   - 之前的讨论中，参与者对补丁的必要性表示认可，但也提出了将 KVM 相关函数放入非 KVM 头文件中的潜在问题，认为应该为 KVM 和 PMU 驱动接口创建单独的头文件。

3. **本周的新讨论与进展**：
   - 本周的讨论中，Colton Lewis 继续推进补丁，并提出第二个补丁（PATCH 2/2），旨在重新整理 `asm/arm_pmuv3.h` 和 `perf/arm_pmuv3.h` 之间的依赖关系，以避免不直观的包含顺序。Oliver Upton 对此表示支持，同时指出这有助于改善头文件的直接包含问题。Quentin Perret 也提出了与 pKVM 相关的补丁，解决了权限故障处理中的竞争问题，并得到了其他参与者的认可和应用。

整体来看，邮件讨论围绕着 ARM 架构下 KVM 和 PMU 的代码组织与依赖关系展开，旨在提高代码的可维护性和编译的稳定性。

#### 📝 邮件列表

1. **[02-04 19:57]** [PATCH 1/2] perf: arm_pmuv3: Remove cyclical dependency with kvm_host.h
   - 发件人: Colton Lewis <coltonlewis@google.com>
2. **[02-04 19:57]** [PATCH 2/2] perf: arm_pmuv3: Uninvert dependency between {asm,perf}/arm_pmuv3.h
   - 发件人: Colton Lewis <coltonlewis@google.com>
3. **[02-04 23:52]** Re: [PATCH 1/2] perf: arm_pmuv3: Remove cyclical dependency with
 kvm_host.h
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
4. **[02-05 00:00]** Re: [PATCH 2/2] perf: arm_pmuv3: Uninvert dependency between
 {asm,perf}/arm_pmuv3.h
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
5. **[02-05 18:49]** Re: [PATCH 1/2] perf: arm_pmuv3: Remove cyclical dependency with kvm_host.h
   - 发件人: Colton Lewis <coltonlewis@google.com>
6. **[02-05 18:57]** Re: [PATCH 2/2] perf: arm_pmuv3: Uninvert dependency between {asm,perf}/arm_pmuv3.h
   - 发件人: Colton Lewis <coltonlewis@google.com>
7. **[02-07 14:54]** [PATCH 0/2] Fixes for pKVM NP-guest support
   - 发件人: Quentin Perret <qperret@google.com>
8. **[02-07 14:54]** [PATCH 1/2] KVM: arm64: Improve error handling from check_host_shared_guest()
   - 发件人: Quentin Perret <qperret@google.com>
9. **[02-07 14:54]** [PATCH 2/2] KVM: arm64: Simplify np-guest hypercalls
   - 发件人: Quentin Perret <qperret@google.com>
10. **[02-07 09:58]** Re: [PATCH 0/2] Fixes for pKVM NP-guest support
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
11. **[02-09 10:21]** Re: [PATCH 0/2] Fixes for pKVM NP-guest support
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 8: [PATCH v6 0/4] KVM: arm64: Errata management for VM Live migration

**📧 邮件数**: 11 | **👥 参与者**: 4 | **📅 开始时间**: Wed, 5 Feb 2025 13:22:18 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 ARM64 平台上进行虚拟机实时迁移的错误管理的补丁集（PATCH v6 0/4）。该补丁集的核心是实现对不同 CPU 实现的错误管理支持，以便在虚拟机迁移时能够正确处理与 CPU 相关的错误。

历史讨论中，Shameer Kolothum 提出了多个版本的补丁，逐步解决了参与者的反馈，包括调整超调用（hypercall）以获取目标 CPU 实现的信息，以及确保补丁与现有的 ARM64 体系结构兼容。补丁的主要内容包括修改 MIDR/REVIDR 读取方式、引入新的超调用以检索目标实现信息，以及报告所有 KVM/ARM64 特定的超调用。

在本周的新讨论中，参与者对补丁的实现细节进行了深入探讨。Catalin Marinas 提出了关于固件兼容性的问题，询问在不同平台间迁移时，是否所有机器的固件都需要具备相应的错误处理能力。Marc Zyngier 进一步补充，KVM 可以拦截 SMC（Secure Monitor Call）并为客户机提供相应的支持，但这并不意味着所有实现都能无缝迁移。Oliver Upton 则强调了超调用的用户空间控制，指出需要谨慎处理超调用的广告，以确保系统的安全性和稳定性。

总体而言，该补丁集旨在提升 ARM64 平台上 KVM 的错误管理能力，尽管在实现过程中仍面临一些固件和兼容性挑战。

#### 📝 邮件列表

1. **[02-05 13:22]** [PATCH v6 0/4] KVM: arm64: Errata management for VM Live migration
   - 发件人: Shameer Kolothum <shameerali.kolothum.thodi@huawei.com>
2. **[02-05 13:22]** [PATCH v6 1/4] arm64: Modify _midr_range() functions to read MIDR/REVIDR internally
   - 发件人: Shameer Kolothum <shameerali.kolothum.thodi@huawei.com>
3. **[02-05 13:22]** [PATCH v6 2/4] KVM: arm64: Introduce hypercall support for retrieving target implementations
   - 发件人: Shameer Kolothum <shameerali.kolothum.thodi@huawei.com>
4. **[02-05 13:22]** [PATCH v6 3/4] KVM: arm64: Report all the KVM/arm64-specific hypercalls
   - 发件人: Shameer Kolothum <shameerali.kolothum.thodi@huawei.com>
5. **[02-05 13:22]** [PATCH v6 4/4] arm64: paravirt: Enable errata based on implementation CPUs
   - 发件人: Shameer Kolothum <shameerali.kolothum.thodi@huawei.com>
6. **[02-07 14:08]** Re: [PATCH v6 4/4] arm64: paravirt: Enable errata based on
 implementation CPUs
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
7. **[02-07 14:31]** Re: [PATCH v6 4/4] arm64: paravirt: Enable errata based on implementation CPUs
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[02-07 18:10]** Re: [PATCH v6 4/4] arm64: paravirt: Enable errata based on
 implementation CPUs
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
9. **[02-07 18:17]** Re: [PATCH v6 4/4] arm64: paravirt: Enable errata based on implementation CPUs
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[02-07 10:21]** Re: [PATCH v6 3/4] KVM: arm64: Report all the KVM/arm64-specific
 hypercalls
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
11. **[02-07 10:24]** Re: [PATCH v6 3/4] KVM: arm64: Report all the KVM/arm64-specific
 hypercalls
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 9: [PATCH v2 0/3] KVM/arm64: timer fixes for 6.14

**📧 邮件数**: 8 | **👥 参与者**: 3 | **📅 开始时间**: Tue,  4 Feb 2025 11:00:47 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM/arm64 的定时器修复补丁（PATCH v2 0/3），旨在解决在 6.14 版本中的一些定时器相关问题。Marc Zyngier 提出了三个补丁，主要内容包括：确保在所有情况下正确地启动后台定时器、避免在 EL2 状态中错误地使用 EL1 状态、简化模拟定时器的处理，以及在 E2H 为 0 时使 HV 定时器正确返回未定义（UNDEF）。

在历史讨论中，Marc 指出现有的 NV 定时器代码存在一些性能和功能上的问题，尤其是在处理 EL1 定时器模拟时的错误。补丁的目标是修复这些问题，以提高系统的稳定性和性能。

本周的讨论中，参与者 Dmytro Terletskyi 对所有补丁进行了测试并确认有效，Oliver Upton 也对补丁进行了审核并表示支持。最终，Marc 确认将这些补丁应用到修复分支中，标志着这一系列修复的完成。整体来看，本周的进展表明补丁得到了广泛认可，并成功合并。

#### 📝 邮件列表

1. **[02-04 11:00]** [PATCH v2 0/3] KVM/arm64: timer fixes for 6.14
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[02-04 11:00]** [PATCH v2 1/3] KVM: arm64: timer: Always evaluate the need for a soft timer
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[02-04 11:00]** [PATCH v2 2/3] KVM: arm64: timer: Correctly handle EL1 timer emulation when !FEAT_ECV
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[02-04 11:00]** [PATCH v2 3/3] KVM: arm64: timer: Don't adjust the EL2 virtual timer offset
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[02-04 14:17]** Re: [PATCH v2 1/3] KVM: arm64: timer: Always evaluate the need for a
 soft timer
   - 发件人: Dmytro Terletskyi <Dmytro_Terletskyi@epam.com>
6. **[02-04 14:17]** Re: [PATCH v2 2/3] KVM: arm64: timer: Correctly handle EL1 timer
 emulation when !FEAT_ECV
   - 发件人: Dmytro Terletskyi <Dmytro_Terletskyi@epam.com>
7. **[02-04 07:08]** Re: [PATCH v2 0/3] KVM/arm64: timer fixes for 6.14
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
8. **[02-04 15:12]** Re: [PATCH v2 0/3] KVM/arm64: timer fixes for 6.14
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 10: [PATCH V2 0/7] arm64/boot: Enable EL2 requirements for FEAT_PMUv3p9

**📧 邮件数**: 8 | **👥 参与者**: 1 | **📅 开始时间**: Mon,  3 Feb 2025 10:38:21 +0530

#### 🤖 AI 总结

本邮件讨论的主题是关于 ARM64 架构的补丁系列，旨在为 FEAT_PMUv3p9 启用 EL2 的要求。该补丁系列包含七个部分，主要目的是实现对 PMICNTR_EL0、PMICFILTR_EL0 和 PMUACR_EL1 等寄存器的细粒度陷阱控制，以防止它们在 EL1 中的访问导致陷入 EL2。

在历史讨论中，Anshuman Khandual 提到，之前的讨论中，Rob Herring 提及了 FEAT_FGT2 基于陷阱控制的需求，这为当前补丁提供了背景。补丁的 V2 版本基于 v6.14-rc1，进行了重基和更新，确保与最新的 DDI0601 2024-12 定义一致。

本周的新讨论中，Anshuman Khandual 提交了补丁的各个部分，包括更新 ID_AA64MMFR0_EL1 寄存器字段、添加 HDFGRTR2_EL2、HDFGWTR2_EL2、HFGITR2_EL2 和 HFGRTR2_EL2 的寄存器字段。这些补丁已获得 Eric Auger 和 Mark Brown 的审核。最终，补丁系列的最后一部分详细描述了如何初始化 FEAT_FGT2 基于的细粒度陷阱控制寄存器，以确保 PMICNTR_EL0、PMICFILTR_EL0 和 PMUACR_EL1 的访问不会导致陷入 EL2。

总的来说，本周的讨论集中在补丁的具体实现和审核上，推动了 ARM64 架构在性能监控方面的进展。

#### 📝 邮件列表

1. **[02-03 10:38]** [PATCH V2 0/7] arm64/boot: Enable EL2 requirements for FEAT_PMUv3p9
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
2. **[02-03 10:38]** [PATCH V2 1/7] arm64/sysreg: Update register fields for ID_AA64MMFR0_EL1
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
3. **[02-03 10:38]** [PATCH V2 2/7] arm64/sysreg: Add register fields for HDFGRTR2_EL2
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
4. **[02-03 10:38]** [PATCH V2 3/7] arm64/sysreg: Add register fields for HDFGWTR2_EL2
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
5. **[02-03 10:38]** [PATCH V2 4/7] arm64/sysreg: Add register fields for HFGITR2_EL2
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
6. **[02-03 10:38]** [PATCH V2 5/7] arm64/sysreg: Add register fields for HFGRTR2_EL2
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
7. **[02-03 10:38]** [PATCH V2 6/7] arm64/sysreg: Add register fields for HFGWTR2_EL2
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
8. **[02-03 10:38]** [PATCH V2 7/7] arm64/boot: Enable EL2 requirements for FEAT_PMUv3p9
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>

---

### Thread 11: [PATCH v5 0/4] KVM: arm64: Errata management for VM Live migration

**📧 邮件数**: 5 | **👥 参与者**: 3 | **📅 开始时间**: Fri, 24 Jan 2025 15:17:28 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的虚拟机实时迁移中的错误管理（Errata management）。历史讨论中，Shameer Kolothum 提出了一个补丁（patch v5 0/4），该补丁主要针对在虚拟机迁移过程中处理 MIDR 和 REVIDR 寄存器的问题，增强了对 KVM 超调用服务的检查，并增加了获取目标实现 CPU 版本和数量的超调用。补丁经过多次修改，旨在解决之前讨论中提到的缺陷。

在本周的新讨论中，Sebastian Ott 提出了一个关键问题，指出即使有错误管理补丁，MIDR 和 REVIDR 寄存器仍然是只读的，来宾操作系统无法访问这些寄存器，这将影响不同主机间的迁移。Marc Zyngier 参与讨论，表示需要找到一个合适的测试对象，并建议在保留当前行为的同时，逐步消除这些不变寄存器的影响。他还提到不应捕获 MIDR_EL1 寄存器，只需通过 HCR_EL2.TID1 捕获 REVIDR 和 AIDR。

总体而言，本周的讨论集中在如何有效管理这些寄存器以支持虚拟机的迁移，参与者们积极探讨解决方案。

#### 📝 邮件列表

1. **[01-24 15:17]** [PATCH v5 0/4] KVM: arm64: Errata management for VM Live migration
   - 发件人: Shameer Kolothum <shameerali.kolothum.thodi@huawei.com>
2. **[02-04 17:45]** Re: [PATCH v5 0/4] KVM: arm64: Errata management for VM Live
 migration
   - 发件人: Sebastian Ott <sebott@redhat.com>
3. **[02-04 17:11]** Re: [PATCH v5 0/4] KVM: arm64: Errata management for VM Live migration
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[02-04 18:42]** Re: [PATCH v5 0/4] KVM: arm64: Errata management for VM Live
 migration
   - 发件人: Sebastian Ott <sebott@redhat.com>
5. **[02-04 18:15]** Re: [PATCH v5 0/4] KVM: arm64: Errata management for VM Live migration
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 12: [PATCH] KVM: arm64: nv: Set ISTATUS for emulated timers, If timer expired

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 07 Feb 2025 17:45:33 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的补丁，主要涉及在定时器过期时设置 ISTATUS 的问题。

原始补丁建议在虚拟机运行之前，针对支持的特性集进行限制，以确保在迁移过程中不会出现问题。然而，Marc Zyngier 提出，在限制特性集的同时，可能会导致 ID 寄存器中某些不可写字段的值发生变化，这可能会在恢复时引发故障。

在本周的新讨论中，参与者们探讨了如何使用 vCPU 特性标志来描述 NV（Non-Volatile）特性，包括 FEAT_E2H0 和 FEAT_VHE 之间的选择。Marc Zyngier 强调，KVM_ARM_VCPU_INIT 后向用户空间展示的 ID 寄存器必须准确反映虚拟机实际支持的特性集，避免在 KVM_RUN 之后进行特性掩蔽，以确保用户空间能够正确保存和恢复状态。

Oliver Upton 则指出，特性字段的管理变得复杂，尤其是在某些字段不可写的情况下。他们一致认为，应在早期阶段就明确 NV 的限制，以避免在后续阶段出现问题。

总体而言，本周的讨论集中在如何确保虚拟机特性的一致性和可预测性，以提高 KVM 的稳定性和用户体验。

#### 📝 邮件列表

1. **[02-07 17:45]** Re: [PATCH] KVM: arm64: nv: Set ISTATUS for emulated timers, If timer expired
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[02-07 10:09]** Re: [PATCH] KVM: arm64: nv: Set ISTATUS for emulated timers, If
 timer expired
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[02-07 18:38]** Re: [PATCH] KVM: arm64: nv: Set ISTATUS for emulated timers, If timer expired
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[02-07 11:08]** Re: [PATCH] KVM: arm64: nv: Set ISTATUS for emulated timers, If
 timer expired
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 13: [PATCH v4 09/18] KVM: arm64: Introduce __pkvm_vcpu_{load,put}()

**📧 邮件数**: 4 | **👥 参与者**: 3 | **📅 开始时间**: Mon, 3 Feb 2025 19:50:44 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM（Kernel-based Virtual Machine）在 arm64 架构上引入的补丁，具体是 `__pkvm_vcpu_{load,put}()` 的实现。该补丁的目的是改善虚拟 CPU 的加载和卸载过程。

在历史讨论中，参与者提到当前主线代码在 pKVM 模式下运行 arch_timer_edge_cases 自测时发生崩溃，经过 bisect 后确认是由于该补丁引起的。崩溃日志显示系统在执行过程中出现了内核恐慌，提示无法转储 pKVM nVHE 堆栈跟踪。

在本周的新讨论中，Mark Brown 提到已经发布了修复补丁，但这将导致该机器无法在受保护模式下运行 KVM，尽管这并非其设计目的。Oliver Upton 表示对该功能的预期不够明确，讨论中提到的其他补丁尝试禁用某些功能，但显然并不完整。Quentin Perret 对报告和快速修复表示感谢。

总体来看，本周的讨论集中在对补丁引发的问题的修复及其对系统功能的影响上。

#### 📝 邮件列表

1. **[02-03 19:50]** Re: [PATCH v4 09/18] KVM: arm64: Introduce __pkvm_vcpu_{load,put}()
   - 发件人: Mark Brown <broonie@kernel.org>
2. **[02-03 15:19]** Re: [PATCH v4 09/18] KVM: arm64: Introduce __pkvm_vcpu_{load,put}()
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[02-04 14:32]** Re: [PATCH v4 09/18] KVM: arm64: Introduce __pkvm_vcpu_{load,put}()
   - 发件人: Mark Brown <broonie@kernel.org>
4. **[02-05 09:57]** Re: [PATCH v4 09/18] KVM: arm64: Introduce __pkvm_vcpu_{load,put}()
   - 发件人: Quentin Perret <qperret@google.com>

---

### Thread 14: [PATCH v2] KVM: arm64: Remove cyclical dependency in arm_pmuv3.h

**📧 邮件数**: 3 | **👥 参与者**: 3 | **📅 开始时间**: Thu,  6 Feb 2025 00:17:44 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，旨在消除 `arm_pmuv3.h` 中的循环依赖问题。

**原始补丁内容**：
补丁由 Colton Lewis 提出，主要目的是解决 `asm/kvm_host.h`、`asm/arm_pmu.h` 和 `perf/arm_pmuv3.h` 之间的循环依赖。这种依赖导致在编译时出现混淆，特别是在使用 hypercall 宏时，编译器无法识别其定义。为了解决这个问题，补丁提议将 `asm/kvm_host.h` 中不必要的引用移除，并创建一个新的头文件 `asm/kvm_pmu.h`，仅包含所需的函数声明。

**之前讨论要点**：
在之前的讨论中，Marc Zyngier 对补丁提出了质疑，认为直接使用 `asm/kvm_host.h` 并不合适，并建议使用 `linux/kvm_host.h`。他还指出，创建两个 PMU 相关的头文件并没有明确的理由，认为应基于使用模式进行合理的文件划分，而不是个人便利。

**本周的新讨论与进展**：
本周的讨论中，Colton Lewis 继续推动补丁的讨论，强调解决循环依赖的重要性。Marc Zyngier 则要求提供更详细的理由，说明为什么要将功能分开，并对补丁的合理性表示怀疑。此外，内核测试机器人报告了构建错误，提示需要修复某些函数的声明问题。这表明补丁在实现过程中仍需进一步调整和验证。

#### 📝 邮件列表

1. **[02-06 00:17]** [PATCH v2] KVM: arm64: Remove cyclical dependency in arm_pmuv3.h
   - 发件人: Colton Lewis <coltonlewis@google.com>
2. **[02-06 08:27]** Re: [PATCH v2] KVM: arm64: Remove cyclical dependency in arm_pmuv3.h
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[02-07 07:27]** Re: [PATCH v2] KVM: arm64: Remove cyclical dependency in arm_pmuv3.h
   - 发件人: kernel test robot <lkp@intel.com>

---

### Thread 15: [PATCH v1] arm64: head.S: Do not trap access to MPAMSM_EL1

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Wed,  5 Feb 2025 16:46:27 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 ARM64 架构中对 MPAMSM_EL1 寄存器访问的处理。Fuad Tabba 提出的补丁（PATCH v1）旨在确保在主机模式下不对 MPAMSM_EL1 的访问进行陷阱处理。根据 ARM 文档，MPAM2_EL2 的第 50 位（EnMPAMSM）在为 0 时会陷阱访问 MPAMSM_EL1，因此需要将其设置为 1，以禁用陷阱。

在之前的讨论中，Marc Zyngier 提出对该寄存器在内核中的使用情况表示疑问，指出在当前的内核版本（6.14-rc1）中找不到相关的痕迹。他对在没有完整 MPAM 支持框架的情况下启用对该寄存器的访问表示担忧，认为这可能会导致问题。

本周的讨论中，Fuad 对 Marc 的担忧表示理解，并指出 MPAM 支持在内核中尚未完全实现。他认为该补丁的工作应与添加 MPAM 支持的整体工作相结合，暗示可能有其他开发者（如 James）正在进行相关工作。

总结而言，本周的讨论围绕对 MPAMSM_EL1 寄存器访问的补丁展开，参与者对当前内核中 MPAM 支持的缺乏表示关注，并讨论了补丁与未来 MPAM 支持开发的关系。

#### 📝 邮件列表

1. **[02-05 16:46]** [PATCH v1] arm64: head.S: Do not trap access to MPAMSM_EL1
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[02-05 17:02]** Re: [PATCH v1] arm64: head.S: Do not trap access to MPAMSM_EL1
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[02-06 10:06]** Re: [PATCH v1] arm64: head.S: Do not trap access to MPAMSM_EL1
   - 发件人: Fuad Tabba <tabba@google.com>

---

### Thread 16: [PATCH V2] mm/ptdump: Drop GENERIC_PTDUMP

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Wed,  5 Feb 2025 10:30:39 +0530

#### 🤖 AI 总结

本邮件线程讨论了一个关于 Linux 内核的补丁，主题为「[PATCH V2] mm/ptdump: Drop GENERIC_PTDUMP」。该补丁的主要内容是建议移除 `GENERIC_PTDUMP` 配置选项，理由是该选项并不保护任何代码，而只是用于平台对核心 `ptdump` 的订阅。补丁提议直接使用 `PTDUMP_CORE` 进行平台订阅。

在之前的讨论中，参与者指出 `GENERIC_PTDUMP` 可能导致构建问题，因为它并不确保平台已选择相应的核心功能。Mark Rutland 提出，当前的设计使得 `GENERIC_PTDUMP` 和 `PTDUMP_CORE` 之间的关系不明确，建议将其重命名为 `ARCH_HAS_PTDUMP` 以更好地反映其用途。

本周的新讨论中，Anshuman Khandual 和 Mark Rutland 进一步探讨了补丁的合理性，Rutland 强调了移除 `GENERIC_PTDUMP` 的必要性，并指出在某些情况下，平台并未明确选择 `GENERIC_PTDUMP`，这可能导致构建失败。Khandual 也同意需要明确区分这两个选项，并表示将分离出相关更改以便更清晰地处理。

总的来说，本周的讨论集中在补丁的合理性及其对现有配置选项的影响，参与者们一致认为需要更清晰的结构来管理这些配置。

#### 📝 邮件列表

1. **[02-05 10:30]** [PATCH V2] mm/ptdump: Drop GENERIC_PTDUMP
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
2. **[02-05 10:01]** Re: [PATCH V2] mm/ptdump: Drop GENERIC_PTDUMP
   - 发件人: Mark Rutland <mark.rutland@arm.com>
3. **[02-06 09:51]** Re: [PATCH V2] mm/ptdump: Drop GENERIC_PTDUMP
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>

---

### Thread 17: [PATCH] KVM: arm64: Fix nested S2 MMU structures reallocation

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Tue,  4 Feb 2025 14:55:54 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下修复嵌套 S2 MMU 结构重新分配的问题。

**原始 patch/问题内容**：
Marc Zyngier 提出的补丁旨在修复在为每个虚拟 CPU 动态分配 S2 MMU 结构时可能出现的初始化失败问题。补丁通过提前分配指针并在初始化成功后调整大小，避免了在初始化失败时返回旧指针的问题。

**之前讨论要点**：
本邮件线程没有提供历史讨论的上下文，但补丁是基于之前的一个提交（4f128f8e1aaac），该提交支持多个嵌套的 Stage-2 MMU 结构。

**本周的新讨论、进展或结论**：
在本周的讨论中，Alexander Potapenko 对补丁进行了测试并确认其有效性。Marc Zyngier 随后表示该补丁已被应用到修复列表中，并感谢参与者的贡献。补丁的提交 ID 为 5417a2e9b130a78bf48cb4cf92630efcee5ccf38。整体来看，本周的讨论进展顺利，补丁得到了认可并成功应用。

#### 📝 邮件列表

1. **[02-04 14:55]** [PATCH] KVM: arm64: Fix nested S2 MMU structures reallocation
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[02-04 15:58]** Re: [PATCH] KVM: arm64: Fix nested S2 MMU structures reallocation
   - 发件人: Alexander Potapenko <glider@google.com>
3. **[02-04 15:03]** Re: [PATCH] KVM: arm64: Fix nested S2 MMU structures reallocation
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 18: [PATCH v5 3/5] arm64/hwcap: Describe 2024 dpISA extensions to
 userspace

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 7 Feb 2025 18:37:27 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于一个针对 ARM64 架构的补丁，旨在描述 2024 年 dpISA 扩展对用户空间的影响。补丁的编号为 [PATCH v5 3/5]，主要目的是更新 ARM64 的硬件能力（hwcap）定义，以便用户空间能够识别新扩展。

在之前的讨论中，Mark Rutland 提到该补丁在启用 CONFIG_ARM64_SME 时会导致构建失败，原因是缺少了一些必要的定义。他指出，补丁中有多个硬件能力的定义未能正确添加到 arm64_elf_hwcaps 中，导致编译错误。

在本周的新讨论中，Mark Rutland 反馈了构建失败的问题，并确认他已经提交了一个修复补丁，Will 已经合并了该修复。Rutland 进一步解释，某些特性在 2024 年的架构更新中被移除，因此在补丁应用时未能被测试到。他表示将会发送另一个修复以解决剩余的问题。

总结来看，当前讨论集中在补丁的构建问题及其修复上，反映了开发者在处理新架构扩展时所面临的挑战和解决方案。

#### 📝 邮件列表

1. **[02-07 18:37]** Re: [PATCH v5 3/5] arm64/hwcap: Describe 2024 dpISA extensions to
 userspace
   - 发件人: Mark Rutland <mark.rutland@arm.com>
2. **[02-07 18:51]** Re: [PATCH v5 3/5] arm64/hwcap: Describe 2024 dpISA extensions to
 userspace
   - 发件人: Mark Brown <broonie@kernel.org>

---

### Thread 19: [PATCH v2] KVM: arm64: Remove cyclical dependency in arm_pmuv3.h

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 06 Feb 2025 19:45:51 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM 在 arm64 架构下的一个补丁，旨在移除 `arm_pmuv3.h` 中的循环依赖关系。

**原始补丁内容**：
补丁的目标是解决 `asm/kvm_host.h` 被错误地包含在 `asm/arm_pmuv3.h` 中所导致的循环依赖问题。补丁通过将 `asm/kvm_host.h` 移出 `asm/arm_pmuv3.h`，使得编译器在处理相关代码时不再混淆，从而避免编译错误。

**之前讨论要点**：
在之前的讨论中，参与者 Colton Lewis 提到，当前的包含方式导致编译器在解析时出现问题，并且认为这种循环依赖对开发者体验非常不友好。Marc Zyngier 也同意循环依赖的存在是不合理的，但对补丁的具体实现提出了质疑，认为应该采取更全面的解决方案，而不是简单的修补。

**本周新讨论与进展**：
本周的讨论中，Colton 提出了另一种解决方案，即在 `arm_pmuv3.c` 中使用条件包含来打破循环依赖。Marc 则坚持认为应当进行彻底的重构，提出了将接口和内部实现分开，创建独立的头文件的建议。他还提供了一个重构后的代码示例，表明这种重构并不复杂。最终，Marc 强调了进行全面解决方案的重要性，而不仅仅是临时修补。

#### 📝 邮件列表

1. **[02-06 19:45]** Re: [PATCH v2] KVM: arm64: Remove cyclical dependency in arm_pmuv3.h
   - 发件人: Colton Lewis <coltonlewis@google.com>
2. **[02-07 11:52]** Re: [PATCH v2] KVM: arm64: Remove cyclical dependency in arm_pmuv3.h
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 20: [PATCH] KVM: arm64: Fail protected mode init if no vgic hardware is present

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Mon,  3 Feb 2025 15:15:43 -0800

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的补丁，主题为“如果没有 vgic 硬件，则失败保护模式初始化”。该补丁的主要目的是在系统未实现 vgic-v3 的情况下，阻止 KVM 的初始化，以避免在不支持的硬件上运行保护模式时出现内核崩溃。

在历史讨论中，补丁的背景说明了保护模式依赖于 vgic-v3 的存在，但 KVM 在初始化时未能强制执行这一要求，导致在 GICv2 硬件上运行时出现问题。具体表现为在 vcpu_load() 时出现内核恐慌，无法正常恢复 vgic-v3 的状态。

本周的新讨论中，Oliver Upton 提出了补丁并详细描述了问题及其解决方案，Marc Zyngier 随后确认已将该补丁应用于修复中，并表示感谢。补丁的提交标识为 32392e04cb50d87bb7a6a7d9213f44a1a0961820，标志着这一问题得到了及时的修复。

#### 📝 邮件列表

1. **[02-03 15:15]** [PATCH] KVM: arm64: Fail protected mode init if no vgic hardware is present
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[02-04 10:50]** Re: [PATCH] KVM: arm64: Fail protected mode init if no vgic hardware is present
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 21: [PATCH v2] KVM: arm64: Remove cyclical dependency in arm_pmuv3.h

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 07 Feb 2025 17:40:27 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于一个补丁（patch），其内容为“[PATCH v2] KVM: arm64: 移除 arm_pmuv3.h 中的循环依赖”。该补丁旨在解决 KVM（Kernel-based Virtual Machine）在 arm64 架构下的代码依赖问题，具体是去除文件之间的循环引用，以提高代码的可维护性和清晰度。

在历史讨论中并没有相关的内容，因此本周的新讨论成为了主要焦点。本周的邮件由 Colton Lewis 发出，回复了 Marc Zyngier 的意见。Colton 表达了对之前讨论的理解，并表示同意对代码进行调整的必要性。他承认这个修改并不复杂，只是需要重新组织一些代码，并对之前可能引起的误解表示歉意。他强调了自己希望通过精确的修改来传达变更的意图，并承诺在未来的工作中会更加注重代码的优雅性。

总体来看，本周的讨论集中在对补丁的认可和对代码改进方法的反思上，显示出参与者对提升代码质量的共同关注。

#### 📝 邮件列表

1. **[02-07 17:40]** Re: [PATCH v2] KVM: arm64: Remove cyclical dependency in arm_pmuv3.h
   - 发件人: Colton Lewis <coltonlewis@google.com>

---

## 📌 RFC

共 3 个 thread

---

### Thread 1: [RFC PATCH 0/2] Add NV Selftest cases

**📧 邮件数**: 9 | **👥 参与者**: 2 | **📅 开始时间**: Thu,  6 Feb 2025 08:41:18 -0800

#### 🤖 AI 总结

本邮件讨论的主题是关于为 KVM（Kernel-based Virtual Machine）添加 NV（Nested Virtualization）自测用例的 RFC（请求反馈补丁）系列。

1. **原始补丁内容**：
   本系列补丁包含两个主要部分：第一个补丁添加了在 vEL2（作为客体虚拟机监控器运行的环境）中执行客体代码的自测用例，第二个补丁则测试在启用 NV 时，客体代码对 VNCR（Virtual Non-Canonical Registers）映射寄存器的访问。

2. **之前讨论要点**：
   在之前的讨论中，参与者探讨了如何确保测试的有效性，特别是如何验证寄存器访问是否符合架构规则。Marc Zyngier 提出，简单地测试寄存器的读写并不能保证正确性，测试应考虑客体的配置和预期结果。

3. **本周的新讨论与进展**：
   本周的讨论集中在补丁的具体实现和测试细节上。Ganapatrao Kulkarni 提到将添加更多寄存器的设置以确保测试在 VHE（Virtualization Host Extensions）模式下运行。Marc Zyngier 强调了测试的架构一致性，建议在测试中引入对寄存器访问的有效性检查。此外，Kulkarni 表示将尝试使现有测试能够在 EL2 客体中运行，并计划调试现有测试中出现的问题。整体来看，讨论推动了补丁的进一步完善和测试用例的细化。

#### 📝 邮件列表

1. **[02-06 08:41]** [RFC PATCH 0/2] Add NV Selftest cases
   - 发件人: Ganapatrao Kulkarni <gankulkarni@os.amperecomputing.com>
2. **[02-06 08:41]** [RFC PATCH 1/2] KVM: arm64: nv: selftests: Add guest hypervisor test
   - 发件人: Ganapatrao Kulkarni <gankulkarni@os.amperecomputing.com>
3. **[02-06 08:41]** [RFC PATCH 2/2] KVM: arm64: nv: selftests: Access VNCR mapped registers
   - 发件人: Ganapatrao Kulkarni <gankulkarni@os.amperecomputing.com>
4. **[02-06 22:15]** Re: [RFC PATCH 0/2] Add NV Selftest cases
   - 发件人: Ganapatrao Kulkarni <gankulkarni@os.amperecomputing.com>
5. **[02-06 17:30]** Re: [RFC PATCH 2/2] KVM: arm64: nv: selftests: Access VNCR mapped registers
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[02-06 21:14]** Re: [RFC PATCH 1/2] KVM: arm64: nv: selftests: Add guest hypervisor test
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[02-07 18:56]** Re: [RFC PATCH 1/2] KVM: arm64: nv: selftests: Add guest hypervisor
 test
   - 发件人: Ganapatrao Kulkarni <gankulkarni@os.amperecomputing.com>
8. **[02-07 13:59]** Re: [RFC PATCH 1/2] KVM: arm64: nv: selftests: Add guest hypervisor test
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[02-07 22:16]** Re: [RFC PATCH 1/2] KVM: arm64: nv: selftests: Add guest hypervisor
 test
   - 发件人: Ganapatrao Kulkarni <gankulkarni@os.amperecomputing.com>

---

### Thread 2: [RFC PATCH v2 0/4] PMU partitioning driver support

**📧 邮件数**: 5 | **👥 参与者**: 1 | **📅 开始时间**: Sat,  8 Feb 2025 02:01:07 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 ARM PMUv3 驱动的 PMU 分区支持的 RFC PATCH v2，共包含四个补丁。该补丁系列的主要目的是通过利用 MDCR_EL2.HPMN 寄存器字段，将 PMU 计数器分为两个独立的范围，从而允许 KVM 客户机直接访问部分 PMU 功能，降低性能监控的开销。

在历史讨论中，补丁的初步版本（v1）已经提出了分区的基本概念，但由于功能尚不完善，因此以 RFC 形式发布以征求反馈。补丁的主要内容包括对 PMU 计数器的通用化、引入模块参数以设置分区、确保驱动在客户机计数器分区之外工作等。

本周的新讨论中，Colton Lewis 提出了补丁的更新版本（v2），包括：
1. 修正了与 KVM 处理 MDCR_EL2 的相关代码，并确保驱动在 32 位 ARM 上正确编译。
2. 明确了分区仅限于 VHE 模式，并讨论了运行时参数配置的复杂性。
3. 解决了与 sysreg 掩码重用的讨论，强调了在不同架构下的实现差异。
4. 最后，补丁确保客户机只能访问其可用的计数器，进一步增强了系统的安全性和性能。

总体而言，本周的讨论集中在补丁的细节修改和实现可行性上，目标是为 KVM 提供更高效的 PMU 访问方式。

#### 📝 邮件列表

1. **[02-08 02:01]** [RFC PATCH v2 0/4] PMU partitioning driver support
   - 发件人: Colton Lewis <coltonlewis@google.com>
2. **[02-08 02:01]** [RFC PATCH v2 1/4] perf: arm_pmuv3: Generalize counter bitmasks
   - 发件人: Colton Lewis <coltonlewis@google.com>
3. **[02-08 02:01]** [RFC PATCH v2 2/4] perf: arm_pmuv3: Introduce module param to
 partition the PMU
   - 发件人: Colton Lewis <coltonlewis@google.com>
4. **[02-08 02:01]** [RFC PATCH v2 3/4] perf: arm_pmuv3: Keep out of guest counter partition
   - 发件人: Colton Lewis <coltonlewis@google.com>
5. **[02-08 02:01]** [RFC PATCH v2 4/4] KVM: arm64: Make guests see only counters they can access
   - 发件人: Colton Lewis <coltonlewis@google.com>

---

### Thread 3: [RFC PATCH 1/4] perf: arm_pmuv3: Introduce module param to
 partition the PMU

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 03 Feb 2025 21:37:24 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于在 ARM PMU（性能监控单元）中引入模块参数以实现 PMU 的分区。该补丁（patch）旨在增强性能监控功能，允许对 PMU 进行更灵活的管理。

在历史讨论中，尚未有具体的讨论内容，因此本周的新讨论成为了主要焦点。Colton Lewis 在邮件中指出，实现该功能在 EL1（异常级别1）下比在 EL2（异常级别2）下更为复杂，因为一旦 HPMN（硬件性能监控网络）生效，主机使用的计数器上限范围只能在 EL2 下进行写入。这意味着涉及到上限范围内任何计数器的寄存器操作都需要通过超调用（hypercall）来实现。他提到，虽然通常不希望在 VHE（虚拟化硬件扩展）和 nVHE 模式之间存在功能差异，但 Oliver 认为在此情况下，限制 PMU 分区仅在 VHE 模式下使用可能是合理的。

综上所述，本周的讨论主要集中在 PMU 分区在不同异常级别下的实现复杂性及其可能的设计选择上。

#### 📝 邮件列表

1. **[02-03 21:37]** Re: [RFC PATCH 1/4] perf: arm_pmuv3: Introduce module param to
 partition the PMU
   - 发件人: Colton Lewis <coltonlewis@google.com>

---

## 📌 Question

共 1 个 thread

---

### Thread 1: Question about lock_all_vcpus

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 06 Feb 2025 15:08:10 -0500

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（内核虚拟机）在 ARM 架构中使用的 `lock_all_vcpus` 函数。Maxim Levitsky 提出了一个问题，指出在某些情况下，该函数可能导致锁定深度超出最大限制，进而引发 CI（持续集成）失败。具体来说，系统报告了一个关于锁定深度的错误，显示当前的 `MAX_LOCK_DEPTH` 为 48，而虚拟 CPU（vCPU）的数量可能达到数百，从而引发锁定冲突。

在历史讨论中，虽然没有具体的邮件记录，但可以推测 `lock_all_vcpus` 函数主要用于初始化阶段，且在 x86 架构中，类似的情况通过确保用户空间在创建或运行第一个 vCPU 之前调用相关函数来避免了这种锁定需求。

本周的讨论中，Levitsky 提出了两个可能的解决方案：一是探讨是否有可能去除 `lock_all_vcpus` 函数以避免该问题，二是考虑将其排除在锁定依赖验证器（lockdep validator）之外。他还提到，x86 架构最近进行了许多清理工作，以确保用户空间在 vCPU 运行后不会更改 CPUID，从而减少了对锁定的需求。

#### 📝 邮件列表

1. **[02-06 15:08]** Question about lock_all_vcpus
   - 发件人: Maxim Levitsky <mlevitsk@redhat.com>

---

## 📌 GIT PULL

共 1 个 thread

---

### Thread 1: [GIT PULL] KVM/arm64 fixes for 6.14, take #1

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Tue,  4 Feb 2025 15:56:56 +0000

#### 🤖 AI 总结

本邮件讨论主题为“KVM/arm64 fixes for 6.14, take #1”，主要涉及针对 Linux 内核 6.14 版本的 KVM/arm64 修复补丁。

1. **原始 patch/问题的内容**：本次补丁集主要修复了在合并窗口中引入的代码所暴露的问题，包括定时器、调试和受保护模式等方面的缺陷。补丁内容包括清理 BSS 段、修复调试寄存器的所有权传播、确保受保护模式的初始化依赖于 GICv3 硬件、解决 vcpu 初始化失败导致的内存释放问题等。

2. **之前的讨论要点**：本次邮件没有提供历史讨论的背景信息，主要集中在当前补丁的提交和修复内容上。

3. **本周的新讨论、进展或结论**：Marc Zyngier 提交了补丁请求，并详细列出了修复内容。Paolo Bonzini 对补丁请求表示确认并表示感谢，表明补丁已被接受。

总的来说，本周的讨论集中在 KVM/arm64 的修复补丁上，Marc Zyngier 提交的补丁得到了快速的确认和接受，显示出开发者对修复工作的重视和高效的沟通。

#### 📝 邮件列表

1. **[02-04 15:56]** [GIT PULL] KVM/arm64 fixes for 6.14, take #1
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[02-06 10:39]** Re: [GIT PULL] KVM/arm64 fixes for 6.14, take #1
   - 发件人: Paolo Bonzini <pbonzini@redhat.com>

---

## 📌 Other

共 1 个 thread

---

### Thread 1: [kvm-unit-tests PATCH] arm: pmu: Actually use counter 0 in test_event_counter_config()

**📧 邮件数**: 3 | **👥 参与者**: 3 | **📅 开始时间**: Mon,  3 Feb 2025 10:10:26 -0800

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM 单元测试的补丁，主题为“arm: pmu: 实际使用计数器 0 在 test_event_counter_config() 中”。该补丁的目的是修正测试函数中错误地使用计数器 1 的问题，确保一致性地使用计数器 0，以便在 Apple 硅的 KVM PMUv3 模拟中能够通过测试，因为该硬件仅提供一个事件计数器。

在历史讨论中，补丁的背景没有详细记录，但可以推测之前的实现未能考虑到特定硬件的限制，导致测试未能正确通过。

在本周的新讨论中，Oliver Upton 提出了该补丁，并解释了问题所在。Eric Auger 对补丁进行了审核并表示感谢，确认了修复的必要性。随后，Andrew Jones 宣布该补丁已被合并，标志着问题的解决和进展。

总结而言，本周的讨论集中在修复 KVM 测试中的计数器使用错误上，得到了参与者的认可并成功合并。

#### 📝 邮件列表

1. **[02-03 10:10]** [kvm-unit-tests PATCH] arm: pmu: Actually use counter 0 in test_event_counter_config()
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[02-04 08:44]** Re: [kvm-unit-tests PATCH] arm: pmu: Actually use counter 0 in
 test_event_counter_config()
   - 发件人: Eric Auger <eric.auger@redhat.com>
3. **[02-04 14:20]** Re: [kvm-unit-tests PATCH] arm: pmu: Actually use counter 0 in
 test_event_counter_config()
   - 发件人: Andrew Jones <andrew.jones@linux.dev>

---

